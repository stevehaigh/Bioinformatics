
"""
    Get the most frequent k-mers for a given k from an input string
"""

import sys


def read_string_and_k_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    sequence, k = open(filename).readlines()

    # Remove any trailing whitespace
    sequence = sequence.strip()

    # ensure k really is an int
    k = int(k)

    return sequence, k


def build_kmer_map(sequence, k):
    """
    :param sequence: A string of bases.
    :param k: Length of the k-mers to build.
    :return: A map of each k-mer and associated count.
    """

    # Built the map for all possible k-mers with their counts
    kmers = {}

    for i in range(len(sequence) - k):
        current_kmer = sequence[i: i + k]
        if kmers.has_key(current_kmer):
            kmers[current_kmer] += 1
        else:
            kmers[current_kmer] = 1

    return kmers


def find_most_freq_kmers(map):
    """

    :rtype : list of strings
    :param map: a map (hash table / dictionary) of kmers with counts
    :return: a list of the most frequently occuring kmers (could be more than one
    """

    # Now search map for high scorers, there could be more than one.
    high_score = 0
    found_kmers = []

    for kmer, count in map.iteritems():
        if count > high_score:
            # new high scoring kmer so replace the found values
            high_score = count
            found_kmers = [kmer]
        elif count == high_score:
            # another kmer with the saem score, so keep this too
            found_kmers.append(kmer)

    return found_kmers


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # filename must be 1st arg passed to the script, otherwise blow up here
    # clever command line parsing is a bit over the top here, maybe later
    seq, k = read_string_and_k_from_file(argv[1])
    kmer_map = build_kmer_map(seq, k)
    most_freq_kmers = find_most_freq_kmers(kmer_map)

    print(most_freq_kmers)


if __name__ == "__main__":
    sys.exit(main())
