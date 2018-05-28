import requests

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
