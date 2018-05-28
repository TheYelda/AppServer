import json
from . import *


def retrieve_a_job(job_id, expected_code, expected_data):
    func_name = 'retrieve a single job'
    url = "{}/{}".format(jobs_url, job_id)
    resp = session.get(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_data:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)


def edit_a_job(job_id, expected_code, data, expected_data):
    func_name = 'edit a job'
    url = "{}/{}".format(jobs_url, job_id)
    resp = session.put(url, data)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_data:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)


def del_a_job(job_id, expected_code):
    func_name = 'del a job'
    url = "{}/{}".format(jobs_url, job_id)
    resp = session.delete(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        succeed(func_name)


def list_all_jobs(expected_code, image_id=None, account_id=None, job_state=None, expected_data=None):
    func_name = 'list all jobs'
    url = "{}/?".format(jobs_url)
    if image_id is not None:
        image_id_url = "image_id={}".format(image_id)
    else:
        image_id_url = ''
    if account_id is not None:
        account_id_url = 'account_id={}'.format(account_id)
    else:
        account_id_url = ''
    if job_state is not None:
        jobs_state_url = 'job_state={}'.format(job_state)
    else:
        jobs_state_url = ''

    # TODO: how to write URL for listing all jobs
    url += '&'.join([image_id_url, account_id_url, jobs_state_url])

    resp = session.get(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_data:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)


def create_a_job(expected_code, data, expected_data):
    func_name = 'create a job'
    url = "{}".format(jobs_url)
    resp = session.post(url, data)
    if resp.status_code != expected_code:
        error(func_name, 'expected code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_data:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)
