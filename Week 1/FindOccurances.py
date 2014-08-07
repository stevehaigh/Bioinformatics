"""
aka Pattern Matching
"""

import sys


def read_kmer_and_sequence_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    kmer, sequence = open(filename).readlines()

    kmer = kmer.strip()
    sequence = sequence.strip()

    return kmer, sequence


def find_all_matches(sequence, kmer):
    """
    :param sequence: a string in which to search for matches (e.g. a genetic sequence)
    :param kmer:  the string to search for (e.g. a shorter sequence)
    :return: an generator over indexes where the match was found
    """
    start = 0
    while True:
        start = sequence.find(kmer, start)
        if start == -1: return
        yield str(start)
        start += 1


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    kmer, sequence = read_kmer_and_sequence_from_file(argv[1])

    result = find_all_matches(sequence, kmer)

    print " ".join(list(result))


if __name__ == "__main__":
    sys.exit(main())
