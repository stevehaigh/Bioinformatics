"""
    File: FreqWordsWithMismatches
    Author: steve
    Created: 10/08/2014
    
"""
import sys
import Tools.SequenceUtils as utils


def read_data_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """
    if not filename:
        return "ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1

    with open(filename) as contents:
        lines = contents.readlines()
        sequence = lines[0].strip()
        k, d = lines[1].split(" ")
        k = int(k)
        d = int(d)

    return sequence, k, d


def find_maxes(kmers):
    """
    Finds the most frequently occuring k-mers in a list.
    :param kmers: a list of k-mers with counts
    :return: the most frequently occuring k-mer(s).
    """
    max_value = max(kmers.values())
    result = [item[0] for item in kmers.items() if item[1] == max_value]
    return result


def find_freq_words_with_mismatches_etc(seq, k, d):
    """
    get all kmers of length k
    :param seq: sequence of bases to search
    :param k: length of k-mer
    :param d: number of mismatches per k-mer
    :return: the most frequently occurring k-mers with mismatches and compliments.
    """
    kmers = utils.find_freq_words_with_mismatches_and_reverse_compliments(seq, k, d)
    result = find_maxes(kmers)
    return result


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv
    seq, k, d = read_data_from_file(argv[1])
    result = find_freq_words_with_mismatches_etc(seq, k, d)
    print(" ".join(result))


if __name__ == "__main__":
    sys.exit(main())