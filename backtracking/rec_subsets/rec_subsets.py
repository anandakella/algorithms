"""rec_subsets.py

use the python3 to run this code
python3 rec_subsets.py
"""


def rec_subsets(so_far, rest):
    """This method finds the possible combinations for given string

    :param so_far: possible combinations of string.
    :type so_far: str
    :param rest: specify the actual string.
    :type rest: str
    :returns: None
    :raises: None
    """
    if not rest:
        print(so_far)
    else:
        # include the first char
        rec_subsets(so_far + rest[0], rest[1:])
        # exclude the first char
        rec_subsets(so_far, rest[1:])


def main():
    """Main function
    """
    a = 'Good'
    rec_subsets("", a)


if __name__ == '__main__':
    main()
