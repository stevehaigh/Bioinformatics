"""
"""

import sys


def read_string_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    with open(filename) as contents:
        foo = contents.readlines()

    return foo


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv


if __name__ == "__main__":
    sys.exit(main())
