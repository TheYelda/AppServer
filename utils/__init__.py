import requests
import json

session = requests.session()
# 设置请求头信息
session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                   'Accept': 'application/json'}

base_url = 'http://localhost:10087'
self_url = "{}/self/".format(base_url)
authorization_url = "{}/authorization/".format(base_url)
account_url = "{}/accounts/".format(base_url)
jobs_url = "{}/jobs/".format(base_url)
images_url = "{}/images/".format(base_url)
label_url = "{}/label/".format(base_url)


def error(func_name, error_info, expected, real, message):
    raise Exception("[Failed] {} : {} \n Expected:{} Reality:{} \n message{}".
                    format(func_name, error_info, expected, real, message))


def succeed(func_name):
    print("[Succeed] {}".format(func_name))


def retrieve_self(expected_code, expected_data=None):
    func_name = 'retrieve_self'
    resp = session.get(self_url)
    code = resp.status_code
    data = json.loads(resp.text)
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        if expected_code == 200:
            if compare_json(expected_data, data):
                succeed(func_name)
            else:
                error(func_name, 'expected id', expected_data, data, data)
        else:
            succeed(func_name)


def remove_authorization(expected_code):
    func_name = 'remove_authorization'
    resp = session.delete(authorization_url)
    data = json.loads(resp.text)
    code = resp.status_code
    if expected_code == code:
        succeed(func_name)
    else:
        error(func_name, 'status code', expected_code, code, data)


def create_authorization(data, expected_code, expected_data):
    func_name = 'create_authorization'
    resp = session.post(authorization_url, json=data)
    data = json.loads(resp.text)
    code = resp.status_code
    if expected_code != code:
        error(func_name, 'status code', expected_code, code, data)
    else:
        if expected_code == 200:
            if compare_json(expected_data, data):
                succeed(func_name)
                return {
                    'remember_token': resp.cookies['remember_token'],
                    'session': resp.cookies['session']
                }
            else:
                error(func_name, 'expected data', expected_data, data, data)
        else:
            succeed(func_name)
            return {}


def compare_json(expected, real):
    for each in expected:
        if expected[each] != real[each]:
            return False
    return True


def test(id, func):
    print("[Testing {}]...".format(id))
    func()
    print("\033[32;1m[Testing {}] Succeed!\033[0m".format(id))
    print()

if __name__ == '__main__':
    expected = {
        'name': '132',
        'password': '123'
    }
    real = {
        'message': '123',
        'name': '132',
        'password': '123'
    }
    compare_json(expected, real)
