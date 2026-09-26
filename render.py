"""Html version of the Simple Remotive job application project"""

import html
import webbrowser
from pathlib import Path

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Remote Jobs</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem; color: #222; }}
  h1 {{ font-size: 1.5rem; }}
  .count {{ color: #666; margin-bottom: 1.5rem; }}
  .job {{ border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 0.75rem; }}
  .job h2 {{ font-size: 1.1rem; margin: 0 0 0.25rem; }}
  .job h2 a {{ color: #1a56db; text-decoration: none; }}
  .job h2 a:hover {{ text-decoration: underline; }}
  .meta {{ color: #555; font-size: 0.9rem; }}
</style>
</head>
<body>
<h1>Remote Jobs</h1>
<p class="count">{count} jobs available</p>
{cards}
</body>
</html>
"""

CARD = """<div class="job">
  <h2><a href="{url}" target="_blank" rel="noopener">{title}</a></h2>
  <div class="meta">{company} &middot; {location} &middot; Posted {date}</div>
</div>"""


def render_jobs(jobs, path="jobs.html", open_browser=True):
    """Write jobs to an HTML file and optionally open it."""
    cards = []
    for job in jobs:
        cards.append(CARD.format(
            url=html.escape(job.get("url", "#")),
            title=html.escape(job.get("title", "Untitled")),
            company=html.escape(job.get("company_name", "Unknown company")),
            location=html.escape(job.get("candidate_required_location") or "Anywhere"),
            date=html.escape(job.get("publication_date", "")[:10]),
        ))

    page = PAGE.format(count=len(jobs), cards="\n".join(cards))
    out = Path(path)
    out.write_text(page, encoding="utf-8")
    print(f"Saved {len(jobs)} jobs to {out.resolve()}")

    if open_browser:
        webbrowser.open(out.resolve().as_uri())