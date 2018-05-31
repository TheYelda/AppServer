import json
from . import *


def retrieve_a_image(image_id, expected_code, expected_data):
    func_name = 'retrieve an image'
    url = '{}/{}'.format(images_url, image_id)
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


def edit_a_image(image_id, expected_code, expected_data):
    func_name = 'edit an image'
    url = "{}/{}".format(images_url, image_id)
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


def del_a_image(image_id, expected_code):
    func_name = 'del an image'
    url = '{}/{}'.format(images_url, image_id)
    resp = session.delete(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        succeed(func_name)


def list_all_image(expected_code, expected_data):
    func_name = 'list all images'
    url = '{}'.format(images_url)
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


def create_a_image(data, expected_code, expected_data):
    func_name = 'create an image'
    url = "{}".format(images_url)
    resp = session.post(url, data)
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
