# -*- coding: utf-8 -*-

"""Main module."""
def is_isbn(isbn: str) -> bool:
    '''
    Check if a given ISBN is valid.

    Input type is str.
    In other cases the function will attempt to convert provided argument to a str.
    In case of an error the return value will be False.

    Returns either True or False depending on the result.
    '''

    # Test ISBN must be provided as a string
    if not isinstance(isbn, str):
        try:
            isbn = str(isbn)
        except:
            return False

    # Clean the test string of any delimiters, typos or spaces if they exist.
    isbn = ''.join(filter(lambda x: x.isdigit(), isbn))

    # ISBN must be either 10 or 13 characters long
    if len(isbn) != 10 and len(isbn) != 13:
        return False

    if len(isbn) == 10:
        return check_isbn_10(isbn)

    elif len(isbn) == 13:
        return check_isbn_13(isbn)


def check_isbn_10(isbn: str) -> bool:
    sum = 0
    for index, value in enumerate(isbn[::-1]):
        sum = sum + (index + 1) * int(value)

    return True if sum % 11 == 0 else False


def check_isbn_13(isbn: str) -> bool:
    sum = 0
    for index, value in enumerate(isbn[::-1]):
        if (index + 1) % 2 == 0:
            sum = sum + int(value) * 3
        else:
            sum = sum + int(value)

    return True if sum % 10 == 0 else False
