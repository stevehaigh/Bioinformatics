import sys
import time


def read_strings_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """

    seq = open(filename).readlines()

    seq = seq[0].strip()
    ## k, L, t = nums.split()

    k = 9 ## int(k)
    L = 500 ## int(L)
    t = 3 ## int(t)

    return seq, k, L, t


def find_kmers_in_seq(sequence, k, t):
    """
    :param sequence: sequence of bases
    :param k: size of k-mer
    :param t: number to look for
    :return: list of kmers appearing t or more times in seq
    """
    # Build the map for all possible k-mers with their counts
    kmers = {}

    for i in range(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        if current_kmer in kmers:
            kmers[current_kmer] += 1
        else:
            kmers[current_kmer] = 1

    return [kmer for kmer, count in kmers.items() if count >= t]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    seq, k, L, t = read_strings_from_file("e-coli.txt")

    # find kmers of length k occurring in runs of length L and report if there are more than t of them
    if len(seq) < L:
        sys.exit(2)  # can't work with an input less than min length

    start = time.clock()
    clumps = set()
    for i in range(0, len(seq) - L):
        # find k-mers of length k with count > t in sub-sequence from i to i + L
        tempClumps = find_kmers_in_seq(seq[i: i + L], k, t)
        if tempClumps:
            clumps.update(tempClumps)

    ## print(" ".join(clumps))
    duration = start - time.clock()
    print (len(clumps))
    print (duration)



if __name__ == "__main__":
    sys.exit(main())
