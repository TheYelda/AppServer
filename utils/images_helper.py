import json
from . import *


def retrieve_a_image(image_id, expected_code, cookies):
    func_name = 'retrieve an image'
    url = '{}{}'.format(images_url, image_id)
    resp = session.get(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def edit_a_image(image_id, data, expected_code, cookies):
    func_name = 'edit an image'
    url = "{}{}".format(images_url, image_id)
    resp = session.put(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def del_a_image(image_id, expected_code, cookies):
    func_name = 'del an image'
    url = '{}{}'.format(images_url, image_id)
    resp = session.delete(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        succeed(func_name)


def list_all_image(expected_code, cookies):
    func_name = 'list all images'
    url = '{}'.format(images_url)
    resp = session.get(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def create_a_image(data, expected_code, expected_data, cookies):
    func_name = 'create an image'
    url = "{}".format(images_url)
    resp = session.post(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != resp.status_code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        if expected_code == 200:
            if compare_json(expected_data, data):
                succeed(func_name)
            else:
                error(func_name, 'expected data', expected_data, data, data)
        else:
            succeed(func_name)
