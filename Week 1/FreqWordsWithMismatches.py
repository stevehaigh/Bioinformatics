"""
    File: FreqWordsWithMismatches
    Author: steve
    Created: 10/08/2014
    
"""
import sys


def read_data_from_file(filename):
    """
    :rtype : tuple
    :param filename: The name of the file to read.
    :return: The sequence string from the file as a string and the value of k as an integer.
    """
    if not filename:
        # embed simple test data, invoke by passing in empoty string for filename
        return "ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1

    with open(filename) as contents:
        lines = contents.readlines()
        sequence = lines[0].strip()
        k, d = lines[1].split(" ")
        k = int(k)
        d = int(d)

    return sequence, k, d


def find_all_single_letter_permutations(kmer):
    """
    Computes all alternate kmers for a sequence by varying just 1 letter in the sequence.
    :param kmer: A kmer
    :return: All single letter permutations of the k-mer.
    """
    result = []
    for i in range(len(kmer)):
        single_letter_permutations = []
        for b in ['A', 'C', 'G', 'T']:
            if kmer[i] != b:
                single_letter_permutations += [kmer[:i] + b + kmer[i + 1:]]

        result += single_letter_permutations
    return result

# declare dict outside method to act as a cache.
# There may be more elegant or pythonic ways to do this.
cached_similar_kmers = {}
def make_all_permutations_of_kmer(kmer, d):
    """
    Computes all alternate permutations of a k-mer with d mismatches.
    Uses recursion to make it easy to permute several chars.
    Uses a cache to optimise repeated requests.
    :param kmer: The k-mer of interest.
    :param d: The number of mis-matchable characters.
    :return: A dictionary of all possible mismatches of the k-mer.
    """
    if d == 0:
        return [kmer]

    cache_key = kmer + str(d)
    if cache_key not in cached_similar_kmers:
        result = []
        single_letter_permutations = find_all_single_letter_permutations(kmer)
        for permuted in single_letter_permutations:
            result += make_all_permutations_of_kmer(permuted, d - 1)
        cached_similar_kmers[cache_key] = result

    return cached_similar_kmers[cache_key]


def find_kmers_with_mismatches(sequence, k, d):
    """
    Finds all k-mers in the sequence of length k, allowing for up to d mismatches per k-mer.
    :param sequence: Sequence of bases.
    :param k: Size of k-mer
    :param d: Max number of mismatches allowed.
    :return:A dictionary of all kmers and their count allowing for mismatches.
    """
    kmers = {}
    for i in range(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        kmer_and_mismatches = set([current_kmer] + make_all_permutations_of_kmer(current_kmer, d))
        for kmer in kmer_and_mismatches:
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1

    return kmers


def main(argv=None):
    if argv is None:
        argv = sys.argv
    seq, k, d = read_data_from_file(argv[1])

    kmers = find_kmers_with_mismatches(seq, k, d)
    max_value = max(kmers.values())
    result = [item[0] for item in kmers.items() if item[1] == max_value]
    print(" ".join(result))

if __name__ == "__main__":
    sys.exit(main())