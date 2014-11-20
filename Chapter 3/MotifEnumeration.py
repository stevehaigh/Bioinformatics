"""
    File: MotifEnumeration
    Author: steve
    Created: 18/11/14
    
"""
import sys
from builtins import range, set, len, sorted, all, str


cached_similar_kmers = {}


def make_all_permutations_of_kmer(kmer, d):
    """
	Computes all alternate permutations of a k-mer with d mismatches.
	Uses a cache to optimise repeated requests.
    """
    if d == 0:
        return [kmer]

    cache_key = kmer + str(d)
    if cache_key not in cached_similar_kmers:
        result = []
        temp = find_all_single_permutations(kmer)
        for permuted in temp:
            result += make_all_permutations_of_kmer(permuted, d - 1)
        cached_similar_kmers[cache_key] = result

    return cached_similar_kmers[cache_key]


def find_all_single_permutations(seq):
    """
	Computes all alterate kmers for a sequence by varying just 1 letter in the sequence.
	"""
    result = []
    for i in range(len(seq)):
        result += permute_single_letter(seq, i)
    return result


def permute_single_letter(seq, i):
    """
	Find all permutations of a k-mer that are 1 edit away from the original.
	"""
    result = []
    for b in ['A', 'C', 'G', 'T']:
        if seq[i] != b:
            temp = seq[:i] + b + seq[i + 1:]
            result += [temp]

    return result


def find_kmers_with_mismatches(sequence, k, d):
    """
	Finds all k-mers in the sequence of length k, allowing for up to d mismatches per k-mer.
	"""
    kmers = set()
    for i in range(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        kmer_and_mismatches = set([current_kmer] + make_all_permutations_of_kmer(current_kmer, d))
        for kmer in kmer_and_mismatches:
            if not kmer in kmers:
                kmers.add(kmer)

    return kmers


def dna_contains_pattern(pattern, dna, d):
    """
    Check if a dna string contains a pattern with up to d mismatches.
    """
    kmers = set([pattern] + make_all_permutations_of_kmer(pattern, d))

    for kmer in kmers:
        if kmer in dna:
            return True

    return False


def pattern_exists_in_each_dna(pattern, dnas, d):
    """
    Check if a pattern exists in ever dna string in the collection, with d mismatches allowed.
    """
    # for dna in dnas:
    # if not dna_contains_pattern(pattern, dna, d):
    # return False
    #
    # return True

    return all(dna_contains_pattern(pattern, dna, d) for dna in dnas)


def motif_enumeration(dna_collection, k, d):
    """
    :param dna: a list of DNA strings.
    :param k: size of k-mer motifs to look for.
    :param d: number of difference allowed.
    :return: a list of motfis - k-mers appearing in every DNA string subject to at most d difference in bases.
    """

    patterns = set()

    for dna in dna_collection:
        for i in range(len(dna) - k + 1):
            kmer = dna[i: i + k]

            # if kmer or d-permutations exists in all other_dnas with at most d-permutations then it's a motif to keep
            kmers_with_perms = find_kmers_with_mismatches(dna, k, d)

            for pattern in kmers_with_perms:
                if not pattern in patterns:
                    if pattern_exists_in_each_dna(pattern, dna_collection, d):
                        patterns.add(pattern)

    return patterns


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    k = 5
    d = 1
    dna = "GTGATTAAAGCTAACCTGGATCCTG " \
          "AGTGGTGTACGATCTACACCCTGGC " \
          "CTTCCGGGGTATAGATCGGACTGGA " \
          "CATGCTTAGTGCTATCTGGTCCTCA " \
          "CTGGTTTGCGCCTTTTTGATACCAG " \
          "GGCCTCATGACACGTATGCACTGGG" \
        .split(' ')

    result = sorted(motif_enumeration(dna, k, d))
    print(len(result))
    print(" ".join(result))


if __name__ == "__main__":
    sys.exit(main())