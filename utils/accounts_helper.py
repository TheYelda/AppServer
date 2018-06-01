from . import *

session = requests.session()
# 设置请求头信息
session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                   'Accept': 'application/json'}


def retrieve_account(account_id, expected_code, expected_data, cookies):
    url = "{}{}".format(account_url, account_id)
    func_name = 'retrieve_account'
    resp = session.get(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        if expected_code == 200:
            if compare_json(expected_data, data):
                succeed(func_name)
            else:
                error(func_name, 'expected data', expected_data, data, data)
        else:
            succeed(func_name)


def edit_account(account_id, data, expected_code, expected_data, cookies):
    func_name = 'edit_account'
    url = "{}{}".format(account_url, account_id)
    resp = session.put(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, "status code", expected_code, code, data)
    else:
        if expected_code == 200:
            if compare_json(expected_data, data):
                succeed(func_name)
            else:
                error(func_name, 'expected data', expected_data, data, data)
        else:
            succeed(func_name)


def delete_account(account_id, expected_code, cookies):
    func_name = 'delete_account'
    url = "{}{}".format(account_url, account_id)
    resp = session.delete(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        succeed(func_name)


def list_accounts(expected_code, cookies):
    func_name = 'list_accounts'
    url = account_url
    resp = session.get(url, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != resp.status_code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        print(data)
        succeed(func_name)


def create_account(data, expected_code, cookies):
    func_name = 'create_account'
    url = account_url
    resp = session.post(url, json=data, cookies=cookies)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        succeed(func_name)

if __name__ == '__main__':
    # TODO testing...
    pass
