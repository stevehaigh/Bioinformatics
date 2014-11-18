"""
Find clumps. I.e. find k-mers in given sub-strings of a sequence.
"""
import sys
import time


def read_strings_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """
    with open(filename) as contents:
        seq, nums = contents.readlines()

    seq = seq.strip()
    k, L, t = nums.split()
    k = int(k)
    L = int(L)
    t = int(t)

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
            kmers[current_kmer].append(i)
        else:
            kmers[current_kmer] = [i]

    return [(kmer, indices) for kmer, indices in kmers.items() if len(indices) >= t]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    start = time.clock()
    seq, k, L, t = read_strings_from_file("ecoli.txt")

    # find kmers of length k occurring in runs of length L and report if there are more than t of them
    if len(seq) < L:
        sys.exit(2)  # can't work with an input less than min length

    duration = time.clock() - start
    print("file read: ", duration)
    start = time.clock()

    # find k-mers of length k with count > t in sub-sequence from i to i + L
    kmers = find_kmers_in_seq(seq, k, t)

    duration = time.clock() - start
    print("build indexes: ", duration)
    start = time.clock()


    # check for clumping
    indexRange = L - k # if a k-mer has at least t indices in this range it's a clump
    count = 0

    for kmer in kmers:
        # if there are more than t indices with a range L - k then it's a clump
        # print(u"Checking kmer {0:s}".format(kmer[0]))
        indices = kmer[1]
        for i in range(len(indices) - t + 1):
            if (indices[i + t - 1] - indices[i]) <= indexRange:
                count += 1
                ##clumps.add(kmer[0])
                break

    duration = time.clock() - start
    ##print(len(clumps))
    print(count)
    print("find clumps: ", duration)


if __name__ == "__main__":
    sys.exit(main())
