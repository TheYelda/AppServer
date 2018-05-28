import json
from . import *


def retrieve_a_label(label_id, expected_code, expected_data):
    func_name = 'retrieve a label'
    url = "{}/{}".format(label_url, label_id)
    resp = session.get(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_code:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)


def edit_a_label(label_id, expected_code, expected_data):
    func_name = 'edit a label'
    url = '{}/{}'.format(label_url, label_id)
    resp = session.put(url)
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


def del_a_label(label_id, expected_code):
    func_name = 'del a label'
    url = "{}/{}".format(label_url, label_id)
    resp = session.delete(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        succeed(func_name)


def create_a_label(data, expected_code):
    func_name = 'create a label'
    url = "{}".format(label_url)
    resp = session.post(url, data)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text) == data:
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)
