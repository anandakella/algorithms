"""rec_permute.py

use the python3 to run this code
python3 rec_permute.py
"""


def rec_permute(so_far, rest):
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
        for i in range(len(rest)):
            remain = rest[0:i] + rest[i+1:]
            rec_permute(so_far + rest[i], remain)


def main():
    """Main function
    """
    a = 'Hello'
    rec_permute("", a)


if __name__ == '__main__':
    main()
