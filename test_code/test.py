import requests
import json

session = requests.session()
# 设置请求头信息
session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                   'Accept': 'application/json'}

base_url = 'http://202.116.86.64:8080'
self_url = "{}/myself".format(base_url)
authorization_url = "{}/authorization".format(base_url)
account_url = "{}/accounts".format(base_url)
jobs_url = "{}/jobs".format(base_url)
images_url = "{}/images".format(base_url)
label_url = "{}/label".format(base_url)


def error(func_name, error_info):
    raise Exception("[Failed] {} : {} ".format(func_name, error_info))


def succeed(func_name):
    print("[Succeed]{}".format(func_name))


def retrieve_self(expected_code, expected_id):
    func_name = 'retrieve_self'
    resp = session.get(self_url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text)['account_id'] == expected_id:
                succeed(func_name)
            else:
                error(func_name, 'expected id')
        else:
            succeed(func_name)


def remove_authorization(expected_code):
    func_name = 'remove_authorization'
    resp = session.delete(authorization_url)
    if expected_code == resp.status_code:
        succeed(func_name)
    else:
        error(func_name, 'status code')


def create_authorization(username, password, expected_code):
    data = {
        'username': username,
        'password': password
    }
    func_name = 'create_authorization'
    resp = session.post(authorization_url, data=data)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if retrieve_self(200, json.loads(resp.text)['account_id']):
                remove_authorization(204)
            else:
                error(func_name, 'account id')
        else:
            succeed(func_name)


def retrieve_account(username, password, expected_code, request_id):
    create_authorization(username, password, 200)
    url = "{}/{}".format(account_url, request_id)
    func_name = 'retrieve_account'
    resp = session.get(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        if expected_code == 200:
            if json.loads(resp.text)['account_id'] == request_id:
                remove_authorization(204)
            else:
                error(func_name, 'account id')
        else:
            succeed(func_name)


def edit_account(username, password, request_id, expected_code, data, expected_data):
    create_authorization(username, password, 200)
    func_name = 'edit_account'
    url = "{}/{}".format(account_url, request_id)
    resp = session.put(url, data)
    if expected_code != resp.status_code:
        error(func_name, "status code")
    else:
        if expected_code == 200:
            if json.loads(resp.text) == expected_data:
                remove_authorization(204)
                succeed(func_name)
            else:
                error(func_name, 'expected data')
        else:
            succeed(func_name)


def delete_account(username, password, request_id, expected_code, expected_self_code, expected_id):
    create_authorization(username, password, 200)
    func_name = 'delete_account'
    url = "{}/{}".format(account_url, request_id)
    resp = session.delete(url)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        retrieve_self(expected_self_code, expected_id)


def list_accounts(username, password, expected_code, expected_data):
    create_authorization(username, password, 200)
    func_name = 'list_accounts'
    url = account_url
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


def create_account(data, expected_code):
    func_name = 'create_account'
    url = account_url
    resp = session.post(url, data=data)
    if expected_code != resp.status_code:
        error(func_name, 'status code')
    else:
        succeed(func_name)

if __name__ == '__main__':
    raise Exception('[312] 321:321')
