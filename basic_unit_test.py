def string_length(some_string):  # production code
    return len(some_string)


def testing_string_length():  # A unit test
    test_string = "1"  # The setup
    length = string_length(test_string)  # the action call to production code
    assert length == 1  # the assertion
