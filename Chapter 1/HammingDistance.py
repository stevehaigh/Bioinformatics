"""
    File: ApproxMatching
    Author: steve
    Created: 06/08/2014
    
"""
import sys


def read_string_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """
    with open(filename) as contents:
        lines = contents.readlines()

    return lines[0:2]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # #lines = read_string_from_file(argv[1])
    lines = ["CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG",
             "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"]
    count = 0

    for i, (char1, char2) in enumerate(zip(lines[0], lines[1])):
        if char1 != char2:
            count += 1

    print count


if __name__ == "__main__":
    sys.exit(main())