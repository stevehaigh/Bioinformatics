
"""
    Get the most frequent k-mers for a given k from an input string
"""
from sets import Set

import sys
from ApproxMatching import is_approx_match


def read_string_and_k_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    sequence, k, d = open(filename, 'r').readlines()
    # Remove any trailing whitespace
    sequence = sequence.strip()
    # ensure k really is an int
    k = int(k)
    d = int(d)

    return sequence, k, d


def build_kmer_map(sequence, k):
    """
    :param sequence: A string of bases.
    :param k: Length of the k-mers to build.
    :return: A map of each k-mer and associated count.
    """

    # Build the map for all possible k-mers with their counts
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
    :return: a list of the most frequently occurring kmers (could be more than one
    """

    # Now search map for high scorers, there could be more than one.
    high_score = 0
    found_kmers = {}

    for kmer, count in map.iteritems():
        if count > high_score:
            # new high scoring kmer so replace the found values
            high_score = count
            found_kmers = {}
            found_kmers[kmer] = count
        elif count == high_score:
            # another kmer with the same score, so keep this too
            found_kmers[kmer] = count

    return found_kmers


def resolve_mismatches(kmer_map, d):
    """
        For each kmer see if there are any other kmers that nearly match, if so add the counts.
    :param seq:
    :param k:
    :return:
    """

    new_map = {}

    for kmer_a, count_a in kmer_map.iteritems():
        new_map[kmer_a] = count_a
        for kmer_b, count_b in kmer_map.iteritems():
            if kmer_a != kmer_b: # don't compare with self
                if is_approx_match(kmer_a, kmer_a, d):
                    new_map[kmer_a] += count_b

    return new_map


def main(argv = None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # filename must be 1st arg passed to the script, otherwise blow up here
    # clever command line parsing is a bit over the top here, maybe later
    seq, k, d = read_string_and_k_from_file(argv[1])
    kmer_map = build_kmer_map(seq, k)
    kmer_map = resolve_mismatches(kmer_map, d)
    most_freq_kmers = find_most_freq_kmers(kmer_map)
    result = disambiguate(most_freq_kmers, d)

    print(" ".join(result))


if __name__ == "__main__":
    sys.exit(main())
