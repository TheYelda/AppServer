"""
The code for testing `images`.
"""
from utils.images_helper import *


def create_test_1():
    """
    directly create image
    """
    create_a_image(data={
        "filename": "image1.png",
        "source": "someone"
    }, expected_code=401, expected_data=None, cookies={})


def create_test_2():
    """
    admin login
    create images
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
    create_a_image(data={
        "filename": "image1.png",
        "source": "someone"
    }, expected_code=201, expected_data={
        "filename": "image1.png",
        "source": "someone"
    }, cookies=cookies)
    create_a_image(data={
        "filename": "image2.png",
        "source": "someone"
    }, expected_code=201, expected_data={
        "filename": "image2.png",
        "source": "someone"
    }, cookies=cookies)
    create_a_image(data={
        "filename": "image2.png",
        "source": "someone"
    }, expected_code=409, expected_data=None, cookies=cookies)
    remove_authorization(200)


def create_test_3():
    """
    doctor login
    create image
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 1
    })
    create_a_image(data={
        "filename": "image3.png",
        "source": "someone"
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(expected_code=200)


def create_test_4():
    """
    guest login
    create image
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
    create_a_image(data={
        "filename": "image3.png",
        "source": "someone"
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_1():
    """
    directly retrieve image
    """
    retrieve_a_image(1, expected_code=401, cookies={})


def retrieve_test_2():
    """
    admin login
    retrieve image
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
    retrieve_a_image(2, expected_code=200, cookies=cookies)
    remove_authorization(200)


def retrieve_test_3():
    """
    doctor login
    retrieve image
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    retrieve_a_image(1, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_4():
    """
    guest login
    retrieve image
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
    retrieve_a_image(1, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_test_5():
    """
    admin login
    retrieve image which doesn't exist.
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
    retrieve_a_image(10, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_1():
    """
    directly del images
    """
    del_a_image(1, expected_code=401, cookies={})


def del_test_2():
    """
    guest login
    del image
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
    del_a_image(1, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_3():
    """
    doctor login
    del image
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    del_a_image(1, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_4():
    """
    admin login
    del image which doesn't exist
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
    del_a_image(10, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def del_test_5():
    """
    admin login
    del image
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
    del_a_image(1, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_1():
    """
    directly list
    """
    list_all_image(401, cookies={})


def list_test_2():
    """
    admin login
    list images
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
    list_all_image(200, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_3():
    """
    doctor login
    list images
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    list_all_image(200, cookies=cookies)
    remove_authorization(expected_code=200)


def list_test_4():
    """
    guest login
    list images
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
    list_all_image(200, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_1():
    """
    directly edit
    """
    edit_a_image(2, data={
        "label_id": 67,
        "source": "somexxx"
    }, expected_code=401, cookies={})


def edit_test_2():
    """
    guest login
    edit images
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
    edit_a_image(2, data={
        "label_id": 67,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_3():
    """
    doctor login
    edit images
    """
    cookies = create_authorization(data={
        "username": "doctor1",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 1,
        "authority": 102
    })
    edit_a_image(2, data={
        "label_id": 67,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_4():
    """
    admin login
    edit source
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
    edit_a_image(2, data={
        "label_id": None,
        "image_state": 301,
        "source": "somexx"
    }, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_5():
    """
    admin login
    when state == 300
    edit label id
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
    edit_a_image(2, data={
        "label_id": 1,
        "filename": "123",
        "image_state": 300,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_6():
    """
    admin login
    when state == 301
    edit label id
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
    edit_a_image(3, data={
        "label_id": 1,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_7():
    """
    admin login
    when state == 302
    edit label id
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
    edit_a_image(4, data={
        "label_id": 1,
        "source": "somexxx"
    }, expected_code=200, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_8():
    """
    admin login
    when state == 302
    edit label id which doesn't exist
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
    edit_a_image(4, data={
        "label_id": 10,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def edit_test_9():
    """
    admin login
    when state == 303
    edit label
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
    edit_a_image(5, data={
        "label_id": 1,
        "source": "somexxx"
    }, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def create_image_testing():
    print("Create Image Testing...")
    test(1, create_test_1)

    test(2, create_test_2)

    test(3, create_test_3)

    test(4, create_test_4)


def retrieve_image_testing():
    print("Retrieve Image Testing...")
    test(1, retrieve_test_1)

    test(2, retrieve_test_2)

    test(3, retrieve_test_3)

    test(4, retrieve_test_4)

    test(5, retrieve_test_5)


def del_image_testing():
    print("Del image Testing...")
    test(1, del_test_1)

    test(2, del_test_2)

    test(3, del_test_3)

    test(4, del_test_4)

    test(5, del_test_5)


def list_image_testing():
    print("List images Testing...")
    test(1, list_test_1)

    test(2, list_test_2)

    test(3, list_test_3)

    test(4, list_test_4)


def edit_image_testing():
    print("Edit images Testing...")
    test(1, edit_test_1)

    test(2, edit_test_2)

    test(3, edit_test_3)

    test(4, edit_test_4)

    # test(5, edit_test_5)
    #
    # test(6, edit_test_6)
    #
    # test(7, edit_test_7)
    #
    # test(8, edit_test_8)
    #
    # test(9, edit_test_9)


if __name__ == '__main__':
    """
    Succeed
    """
    # create_image_testing()

    """
    Succeed!
    """
    # retrieve_image_testing()

    """
    Succeed!
    """
    # del_image_testing()

    """
    Succeed!
    """
    # list_image_testing()

    """
    Fail!
    """
    edit_image_testing()
