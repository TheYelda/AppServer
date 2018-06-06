from utils.labels_helper import *


def create_test_1():
    """
    directly create
    """
    create_a_label(data={

    }, )

def create_test_2():
    """
    guest create
    """


def create_test_3():
    """
    admin create
    """


def create_test_4():
    """
    doctor create
    """


def retrieve_test_1():
    """
    directly retrieve
    """


def edit_test_1():
    """
    """


def create_testing():
    print("Create Testing...")
    test(1, create_test_1)

    test(2, create_test_2)

    test(3, create_test_3)

    test(4, create_test_4)


if __name__ == '__main__':
    create_testing()
