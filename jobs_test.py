from utils.jobs_helper import *


def create_test_1():
    """
    directly create
    """
    create_a_job(401, data={
        "image_id": 2,
        "account_id": 1
    }, cookies={})


def create_test_2():
    """
    doctor login
    create
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    create_a_job(403, data={
        "image_id": 2,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_3():
    """
    guest login
    create
    """
    cookies = create_authorization(data={
        "username": "guest1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 7,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 7
    })
    create_a_job(403, data={
        "image_id": 2,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_4():
    """
    admin login
    create
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(201, data={
        "image_id": 2,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_5():
    """
    admin login
    account id doesn't exist.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 2,
        "account_id": 8
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_6():
    """
    admin login
    image id doesn't exist.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 30,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_7():
    """
    admin login
    account isn't doctor
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 2,
        "account_id": 7
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_8():
    """
    admin login
    image state isn't 300.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 3,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)

def create_test_9():
    """
    admin login
    image state isn't 300.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 4,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_10():
    """
    admin login
    image state isn't 300.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    create_a_job(400, data={
        "image_id": 5,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_testing():
    print("Create Testing...")
    test(1, create_test_1)

    test(2, create_test_2)

    test(3, create_test_3)

    test(4, create_test_4)

    test(5, create_test_5)

    test(6, create_test_6)

    test(7, create_test_7)

    test(8, create_test_8)

    test(9, create_test_9)

    test(10, create_test_10)

if __name__ == '__main__':
    create_testing()
