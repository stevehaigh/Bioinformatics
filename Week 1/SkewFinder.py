"""
Find positions of min skew in a sequence
"""

import sys


def read_string_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    with open(filename) as contents:
        seq = contents.readlines()[0].strip()

    return seq


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    seq = read_string_from_file(argv[1])

    cur_skew = 0;
    min_skew = 1000;
    skew_pos = []

    for i, b in enumerate(seq):
        if b == 'G':
            cur_skew += 1
        elif b == 'C':
            cur_skew -= 1

        if cur_skew < min_skew:
            min_skew = cur_skew
            skew_pos = [i+1]
        elif cur_skew == min_skew:
            skew_pos.append(i+1)

    print " ".join(str(s) for s in skew_pos)


if __name__ == "__main__":
    sys.exit(main())
