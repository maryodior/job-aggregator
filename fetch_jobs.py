import requests
from render import render_jobs


URL = "https://remotive.com/api/remote-jobs"


def fetch_jobs(category, limit):
    filters = {"category" : category, "limit" : limit}
    response = requests.get(url=URL, params=filters, timeout=10)
    data = response.json()

    jobs = data["jobs"]

    for job in jobs:
        print(job["title"], "|", job["company_name"])

    print(count_jobs(jobs))

    render_jobs(jobs)

    return jobs

def count_jobs(jobs):
    return len(jobs)

jobs = fetch_jobs("software-development", 10)

