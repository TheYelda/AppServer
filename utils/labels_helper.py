import json
from . import *


def retrieve_a_label(label_id, expected_code, cookies):
    func_name = 'retrieve a label'
    url = "{}/{}".format(label_url, label_id)
    resp = session.get(url)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def edit_a_label(label_id, expected_code, cookies):
    func_name = 'edit a label'
    url = '{}/{}'.format(label_url, label_id)
    resp = session.put(url)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def del_a_label(label_id, expected_code, cookies):
    func_name = 'del a label'
    url = "{}/{}".format(label_url, label_id)
    resp = session.delete(url)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def create_a_label(data, expected_code, cookies):
    func_name = 'create a label'
    url = "{}".format(label_url)
    resp = session.post(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != resp.status_code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)
