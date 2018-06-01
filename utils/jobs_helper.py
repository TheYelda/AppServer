from . import *


def retrieve_a_job(job_id, expected_code, cookies):
    func_name = 'retrieve a single job'
    url = "{}{}".format(jobs_url, job_id)
    resp = session.get(url, cookies=cookies)
    data = json.loads(resp.text)
    code = resp.status_code
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def edit_a_job(job_id, expected_code, data, cookies):
    func_name = 'edit a job'
    url = "{}{}".format(jobs_url, job_id)
    resp = session.put(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def del_a_job(job_id, expected_code, cookies):
    func_name = 'del a job'
    url = "{}{}".format(jobs_url, job_id)
    resp = session.delete(url, cookies=cookies)
    data = json.loads(resp.text)
    code = resp.status_code
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def list_all_jobs(expected_code, cookies):
    func_name = 'list all jobs'
    url = "{}".format(jobs_url)

    resp = session.get(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def create_a_job(expected_code, data, cookies):
    func_name = 'create a job'
    url = "{}".format(jobs_url)
    resp = session.post(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)

    if code != expected_code:
        error(func_name, 'expected code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)
