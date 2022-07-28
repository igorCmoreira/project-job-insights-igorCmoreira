from fileinput import close
from multiprocessing.sharedctypes import Value
from .jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    types_jobs = set()
    for job in jobs:
        types_jobs.add(job["job_type"])
    return types_jobs


def filter_by_job_type(jobs, job_type):
    jobs_typed = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_typed.append(job)
    return jobs_typed


def get_unique_industries(path):
    jobs = read(path)
    types_industry = set()
    for job in jobs:
        if len(job["industry"]) != 0:
            types_industry.add(job["industry"])

    return types_industry


def filter_by_industry(jobs, industry):
    jobs_industry = []
    for job in jobs:
        if job['industry'] == industry:
            jobs_industry.append(job)
    return jobs_industry


def get_max_salary(path):
    jobs = read(path)
    salary_max = 0
    for job in jobs:
        if job["max_salary"].isdigit() and int(job["max_salary"]) > salary_max:
            salary_max = int(job["max_salary"])

    return salary_max


def get_min_salary(path):
    jobs = read(path)
    salary_min = get_max_salary(path)
    for job in jobs:
        if job["min_salary"].isdigit() and int(job["min_salary"]) < salary_min:
            salary_min = int(job["min_salary"])

    return salary_min


def matches_salary_range(job, salary):
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("Salary range is not present in job")

    max_salary = job["max_salary"]
    min_salary = job["min_salary"]

    if type(min_salary) != int or type(max_salary) != int:
        raise ValueError("the salarys is not a number")
    if int(min_salary) > int(max_salary):
        raise ValueError("the max_salary is less than min_salary")
    if type(salary) != int:
        raise ValueError("salary is not a number")
    return int(min_salary) <= salary <= int(max_salary)


def filter_by_salary_range(jobs, salary):
    job_filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_filter_salary.append(job)
        except ValueError:
            close
    return job_filter_salary
