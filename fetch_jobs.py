import requests
from render import render_jobs


URL = "https://remotive.com/api/remote-jobs"
params = {
    "category": "software-development",
    "limit": 10
}

def fetch_jobs(category, limit):
    response = requests.get(url=URL, params=params, timeout=10)
    data = response.json()

    jobs = data["jobs"]

    for job in jobs:
        print(job["title"], "|", job["company_name"])

    print(count_jobs(jobs))

    render_jobs(jobs)

    return jobs

def count_jobs(jobs):
    return len(jobs)

jobs = fetch_jobs(params["category"], params["limit"])

