"""
The code for testing `Accounts`.
"""
from utils.accounts_helper import *


def self_test_1():
    """
    Directly retrieve self is Wrong.
    """
    retrieve_self(401, None)


def create_auth_test_1():
    """
    Correct login
    """
    create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        'account_id': 3
    })
    remove_authorization(200)


def create_auth_test_2():
    """
    username wrong.
    """
    create_authorization(data={
        "username": "admin1",
        "password": "123"
    }, expected_code=401, expected_data=None)
    retrieve_self(expected_code=401, expected_data=None)


def create_auth_test_3():
    """
    password wrong
    :return:
    """
    create_authorization(data={
        "username": "admin",
        "password": "1234"
    }, expected_code=401, expected_data=None)
    retrieve_self(expected_code=401, expected_data=None)


def create_auth_test_4():
    """
    None login
    """
    create_authorization(data={
        "username": "None",
        "password": "123"
    }, expected_code=401, expected_data=None)
    retrieve_self(expected_code=401, expected_data=None)


def remove_auth_test_1():
    """
    directly remove auth
    """
    remove_authorization(expected_code=401)


def remove_auth_test_2():
    """
    login correctly
    """
    create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    remove_authorization(expected_code=200)
    retrieve_self(expected_code=401, expected_data=None)


def remove_auth_test_3():
    """
    login fail
    """
    create_authorization(data={
        "username": "admin1",
        "password": "123"
    }, expected_code=401, expected_data=None)
    remove_authorization(expected_code=401)


def retrieve_account_test_1():
    """
    directly retrieve account by id.
    """
    retrieve_account(account_id=3, expected_code=401, expected_data=None, cookies={})


def retrieve_account_test_2():
    """
    admin login
    retrieve my id.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    retrieve_account(account_id=3, expected_code=200, expected_data={
        "account_id": 3,
        "username": "admin",
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_3():
    """
    admin login
    retrieve other's id.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    retrieve_account(account_id=1, expected_code=200, expected_data={
        "account_id": 1,
        "username": "doctor1",
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_4():
    """
    admin login
    retrieve id which doesn't exist.
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    retrieve_account(account_id=20, expected_code=404, expected_data=None, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_5():
    """
    doctor login
    retrieve my id.
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
    retrieve_account(account_id=1, expected_code=200, expected_data={
        "account_id": 1,
        "username": "doctor1",
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_6():
    """
    guest login
    retrieve my id.
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
    retrieve_account(account_id=7, expected_code=200, expected_data={
        "account_id": 7,
    }, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_7():
    """
    doctor login
    retrieve other's id.
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
    retrieve_account(account_id=10, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(expected_code=200)


def retrieve_account_test_8():
    """
    guest login
    retrieve other's id.
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
    retrieve_account(account_id=9, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(expected_code=200)


def del_account_test_1():
    """
    directly del account
    """
    delete_account(10, 401, cookies={})


def del_account_test_2():
    """
    admin login
    del my account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    delete_account(account_id=3, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_account_test_3():
    """
    admin login
    del other's account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    delete_account(account_id=5, expected_code=204, cookies=cookies)
    remove_authorization(expected_code=200)


def del_account_test_4():
    """
    admin login
    del account which doesn't exist
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 3,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 3
    })
    delete_account(account_id=20, expected_code=404, cookies=cookies)
    remove_authorization(expected_code=200)


def del_account_test_5():
    """
    doctor login
    del other's account
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
    delete_account(account_id=2, expected_code=401, cookies=cookies)
    remove_authorization(expected_code=200)


def del_account_test_6():
    """
    doctor login
    del my account
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
    delete_account(account_id=1, expected_code=204, cookies=cookies)
    retrieve_self(expected_code=404, expected_data=None)


def del_account_test_7():
    """
    guest login
    del other's account
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
    delete_account(account_id=6, expected_code=401, cookies=cookies)
    retrieve_self(expected_code=200, expected_data={})


def del_account_test_8():
    """
    guest login
    del my account
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
    delete_account(account_id=7, expected_code=204, cookies=cookies)
    retrieve_self(expected_code=404, expected_data=None)


def create_account_test_1():
    create_account(data={
        "username": "doctor1",
        "nickname": "doctor1",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=201, cookies={})

    create_account(data={
        "username": "doctor1",
        "nickname": "doctor1",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=409, cookies={})

    create_account(data={
        "username": "admin",
        "nickname": "admin",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=201, cookies={})

    create_account(data={
        "username": "admin",
        "nickname": "admin",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=409, cookies={})


def create_account_test_2():
    create_account(data={
        "username": "doctor2",
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=201, cookies={})
    create_account(data={
        "username": "doctor3",
        "nickname": "doctor3",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=201, cookies={})
    create_account(data={
        "username": "guest1",
        "nickname": "guest1",
        "password": "123",
        "email": "yelda100@mail.com"
    }, expected_code=201, cookies={})


def edit_account_test_1():
    """
    directly edit account
    """
    edit_account(10, data={
        "nickname": "Nick",
        "password": "mypass",
        "email": "yelda@mail.com",
        "photo": "photo1.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies={})


def edit_account_test_2():
    """
    admin login
    edit the nickname and authority of mine
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 2
    })
    edit_account(2, data={
        "nickname": "Nick",
        "password": "mypass",
        "email": "yelda@mail.com",
        "photo": "photo1.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_3():
    """
    admin login
    edit the email of my account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 2
    })
    edit_account(2, data={
        "nickname": "admin",
        "password": "123",
        "email": "yelda@sysu.com",
        "photo": "photo1.png",
        "authority": 101
    }, expected_code=200, expected_data={
        "nickname": "admin",
        "email": "yelda@sysu.com",
        "photo": "photo1.png",
        "authority": 101
    }, cookies=cookies)
    remove_authorization(200)


def edit_account_test_4():
    """
    admin login
    edit the nickname of other's account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 2
    })
    edit_account(5, data={
        "nickname": "admin",
        "password": "123",
        "email": "yelda@sysu.com",
        "photo": "photo1.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_5():
    """
    admin login
    edit the authority of other's account
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 2
    })
    edit_account(3, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "123",
        "photo": "123",
        "authority": 103
    }, expected_code=200, expected_data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, cookies=cookies)
    remove_authorization(200)


def edit_account_test_6():
    """
    admin login
    edit the authority of account which doesn't exist
    """
    cookies = create_authorization(data={
        "username": "admin",
        "password": "123"
    }, expected_code=200, expected_data={
        "account_id": 2,
        "authority": 101
    })
    retrieve_self(expected_code=200, expected_data={
        "account_id": 2
    })
    edit_account(20, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=404, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_7():
    """
    doctor login
    edit the authority of my account
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
    edit_account(1, data={
        "nickname": "doctor1",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_8():
    """
    doctor login
    edit the nickname of my account
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
    edit_account(1, data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 102
    }, expected_code=200, expected_data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 102
    }, cookies=cookies)
    remove_authorization(200)


def edit_account_test_9():
    """
    doctor login
    edit the nickname of other's account
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
    edit_account(5, data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_10():
    """
    doctor login
    edit the authority of other's account
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
    edit_account(5, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_11():
    """
    doctor login
    edit the authority of account which doesn't exist
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
    edit_account(20, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_12():
    """
    guest login
    edit the authority of my account
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
    edit_account(1, data={
        "nickname": "guest1",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_13():
    """
    guest login
    edit the nickname of my account
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
    edit_account(7, data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=200, expected_data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, cookies=cookies)
    remove_authorization(200)


def edit_account_test_14():
    """
    guest login
    edit the nickname of other's account
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
    edit_account(5, data={
        "nickname": "doctor0",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 102
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_15():
    """
    guest login
    edit the authority of other's account
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
    edit_account(5, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def edit_account_test_16():
    """
    guest login
    edit the authority of account which doesn't exist
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
    edit_account(10, data={
        "nickname": "doctor2",
        "password": "123",
        "email": "yelda100@mail.com",
        "photo": "default.png",
        "authority": 103
    }, expected_code=401, expected_data=None, cookies=cookies)
    remove_authorization(200)


def list_accounts_test_1():
    """
    directly list accounts
    """
    list_accounts(401, cookies={})


def list_accounts_test_2():
    """
    admin login
    list accounts
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
    list_accounts(200, cookies=cookies)
    remove_authorization(200)


def list_accounts_test_3():
    """
    doctor login
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
    list_accounts(401, cookies=cookies)
    remove_authorization(expected_code=200)


def self_testing():
    print("Self Testing...")
    test(1, self_test_1)


def create_account_testing():
    print("Create Account Testing...")

    test(1, create_account_test_1)

    test(2, create_account_test_2)


def create_auth_testing():
    print("Create Auth Testing...")

    test(1, create_auth_test_1)

    test(2, create_auth_test_2)

    test(3, create_auth_test_3)

    test(4, create_auth_test_4)


def remove_auth_testing():
    print("Remove Auth Testing...")

    test(1, remove_auth_test_1)

    test(2, remove_auth_test_2)

    test(3, remove_auth_test_3)


def retrieve_account_testing():
    print("Retrieve Account Testing...")
    test(1, retrieve_account_test_1)

    test(2, retrieve_account_test_2)

    test(3, retrieve_account_test_3)

    test(4, retrieve_account_test_4)

    test(5, retrieve_account_test_5)

    test(6, retrieve_account_test_6)

    test(7, retrieve_account_test_7)

    test(8, retrieve_account_test_8)


def del_account_testing():
    print("Delete Account Testing...")

    test(1, del_account_test_1)

    test(2, del_account_test_2)

    # test(3, del_account_test_3)

    test(4, del_account_test_4)

    test(5, del_account_test_5)

    # test(6, del_account_test_6)

    test(7, del_account_test_7)

    test(8, del_account_test_8)


def edit_account_testing():
    print("Edit Accounting Testing...")

    test(1, edit_account_test_1)

    test(2, edit_account_test_2)

    test(3, edit_account_test_3)

    test(4, edit_account_test_4)

    test(5, edit_account_test_5)

    test(6, edit_account_test_6)

    test(7, edit_account_test_7)

    test(8, edit_account_test_8)

    test(9, edit_account_test_9)

    test(10, edit_account_test_10)

    test(11, edit_account_test_11)

    test(12, edit_account_test_12)

    test(13, edit_account_test_13)

    test(14, edit_account_test_14)

    test(15, edit_account_test_15)

    test(16, edit_account_test_16)


def list_accounts_testing():
    print("List Accounts Testing...")
    test(1, list_accounts_test_1)

    test(2, list_accounts_test_2)

    test(3, list_accounts_test_3)


if __name__ == '__main__':
    """
    Succeed!
    """
    # self_testing()

    """
    Succeed!
    """
    # create_account_testing()

    """
    Succeed!
    """
    # create_auth_testing()

    """
    Succeed!
    """
    # remove_auth_testing()

    """
    Suucced!
    """
    # retrieve_account_testing()

    """
    Succeed!
    """
    # list_accounts_testing()

    """
    Succeed!
    """
    # edit_account_testing()

    """
    Succeed
    """
    # del_account_testing()
