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
        "account_id": 5,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 5
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
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
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
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
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
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
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
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    create_a_job(400, data={
        "image_id": 2,
        "account_id": 7
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_8():
    """
    admin login
    image state is 301
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    create_a_job(400, data={
        "image_id": 2,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_9():
    """
    admin login
    image state is 302.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    create_a_job(400, data={
        "image_id": 3,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_10():
    """
    admin login
    image state is 303.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    create_a_job(400, data={
        "image_id": 4,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_11():
    """
    admin login
    same image to same account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    create_a_job(400, data={
        "image_id": 2,
        "account_id": 1
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_1():
    """
    directly list
    """
    list_all_jobs(401, cookies={})


def list_test_2():
    """
    guest login
    list
    """
    cookies = create_authorization(data={
        "username": "guest1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 5,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 5
    })
    list_all_jobs(403, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_3():
    """
    doctor login
    list
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    list_all_jobs(403, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_4():
    """
    admin login
    list
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    list_all_jobs(200, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_1():
    """
    directly retrieve job
    """
    retrieve_a_job(1, 401, cookies={})


def retrieve_test_2():
    """
    guest retrieve
    """
    cookies = create_authorization(data={
        "username": "guest1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 5,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 5
    })
    retrieve_a_job(1, expected_code=403, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_3():
    """
    doctor retrieve
    doctor id == account id
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    retrieve_a_job(1, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_4():
    """
    doctor retrieve
    doctor id != account id
    """
    cookies = create_authorization(data={
        "username": "doctor2",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 102
    })
    retrieve_a_job(1, expected_code=403, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_5():
    """
    admin retrieve
    any.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    retrieve_a_job(1, expected_code=200, cookies=cookies)
    retrieve_a_job(2, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_6():
    """
    admin retrieve
    job id doesn't exist.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    retrieve_a_job(10, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_1():
    """
    directly del job
    """
    del_a_job(1, expected_code=404, cookies={})


def del_test_2():
    """
    guest del
    """
    cookies = create_authorization(data={
        "username": "guest1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 5,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 5
    })
    del_a_job(1, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_3():
    """
    doctor del
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    del_a_job(1, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_4():
    """
    admin del
    id doesn't exist.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    del_a_job(2, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_5():
    """
    admin del
    id exist
    state == 201
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    del_a_job(2, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_1():
    """
    directly edit
    """
    edit_a_job(1, expected_code=401, data={
        "label_id": 88,
        "job_state": 204
    }, cookies={})


def edit_test_2():
    """
    guest edit
    """
    cookies = create_authorization(data={
        "username": "guest1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 5,
        "authority": 103
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 5
    })
    edit_a_job(1, expected_code=403, data={
        "label_id": 88,
        "job_state": 204,
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_3():
    """
    admin edit
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 2
    })
    edit_a_job(1, expected_code=403, data={
        "label_id": 88,
        "job_state": 204
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_4():
    """
    doctor edit
    doctor id != user id
    """
    cookies = create_authorization(data={
        "username": "doctor2",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 102
    })
    edit_a_job(1, expected_code=403, data={
        "label_id": 88,
        "job_state": 204
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_5():
    """
    doctor edit
    doctor id == user id
    state != done
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    edit_a_job(1, expected_code=200, data={
        "label_id": 1,
        "job_state": 201
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_6():
    """
    doctor edit
    doctor id == user id
    state != done
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    edit_a_job(1, expected_code=200, data={
        "label_id": 1,
        "job_state": 202
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_7():
    """
    doctor edit
    doctor id == user id
    state == done
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    edit_a_job(1, expected_code=403, data={
        "label_id": 2,
        "job_state": 202
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

    test(11, create_test_11)


def list_testing():
    print("List Testing...")
    test(1, list_test_1)

    test(2, list_test_2)

    test(3, list_test_3)

    test(4, list_test_4)


def retrieve_testing():
    print("Retrieve Testing...")
    test(1, retrieve_test_1)

    test(2, retrieve_test_2)

    test(3, retrieve_test_3)

    test(4, retrieve_test_4)

    test(5, retrieve_test_5)

    test(6, retrieve_test_6)


def del_testing():
    print("Del Testing...")
    test(1, del_test_1)

    test(2, del_test_2)

    test(3, del_test_3)

    test(4, del_test_4)

    test(5, del_test_5)


def edit_testing():
    print("Edit Testing...")
    # test(1, edit_test_1)
    #
    # test(2, edit_test_2)
    #
    # test(3, edit_test_3)
    #
    # test(4, edit_test_4)
    #
    # test(5, edit_test_5)
    #
    # test(6, edit_test_6)
    #
    # test(7, edit_test_7)


if __name__ == '__main__':
    """
    Succeed!
    """
    # create_testing()

    """
    Succeed!
    """
    # list_testing()

    """
    Succeed!
    """
    # retrieve_testing()

    """
    Succeed!
    """
    # edit_testing()

    """
    Not Impl!
    """
    # del_testing()
