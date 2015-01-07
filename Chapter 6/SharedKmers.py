"""
    File: SharedKmers
    Author: steve
    Created: 07/01/15
    
"""
import sys

def reverse_compliment(seq):
    """
	Create a reverse compliment of the specified sequence.
	"""
    return seq[::-1].lower().replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')



def find_shared_kmer_indexes(k, kmer1, kmer2):


    # build a cache fom kmer1 of all kmers and locations, inc. reverse compliments
    kmers = {}
    for i in range(len(kmer1) - k + 1):
        current_kmer = kmer1[i: i + k]
        if current_kmer in kmers:
            kmers[current_kmer] += [i]
        else:
            kmers[current_kmer] = [i]

        reverse = current_kmer[::-1].lower().replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')
        if reverse in kmers:
            kmers[reverse] += [i]
        else:
            kmers[reverse] = [i]

    results = []

    # now look for matches and build up list of index tuples
    for i in range(len(kmer2) - k + 1):
        kmer = kmer2[i: i + k]
        if kmer in kmers:
            for index in kmers[kmer]:
                results.append((index, i))


    return results


def read_from_file():
    lines = open("shared_kmers.txt").readlines()

    return int(lines[0]), lines[1], lines[2]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # k = 3
    # kmer1 = "AAACTCATC"
    # kmer2 = "TTTCAAATC"

    k, kmer1, kmer2 = read_from_file()

    shared_kmer_indexes = find_shared_kmer_indexes(k, kmer1, kmer2)

    for indexes in shared_kmer_indexes:
        print("(" + str(indexes[0]) + ", " + str(indexes[1])+ ")")


if __name__ == "__main__":
    sys.exit(main())