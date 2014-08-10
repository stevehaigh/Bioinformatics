"""
    File: SequenceUtils
    Author: steve
    Created: 09/08/2014

    Tools to map a sequence of bases to an integer using mod 4 arithmetic.

    A -> 0
    C -> 1
    G -> 2
    T -> 3

    E.g. ACCTG = 01132 in base 4 =  64 + 16 + 12 + 2

    
"""

from array import array

def int_value(b):
    if b == 'A': return 0
    elif b == 'C': return 1
    elif b == 'G': return 2
    elif b == 'T': return 3
    else: raise ValueError("Base was not in ACGT.")


def base(i):
    if i == 0: return 'A'
    elif i == 1: return 'C'
    elif i == 2: return 'G'
    elif i == 3: return 'T'
    else: raise ValueError("Number outside range 0 - 3")


def sequence_to_int(seq):
    """
        read string backward, multiplying the base by the ascending power of 4,
        starting at 1 and adding up as we go.
    """

    result = 0
    multiplier = 1

    for c in seq[::-1]:
        result += int_value(c) * multiplier
        multiplier *= 4

    return result


def int_to_sequence(num, length):
    """
        Build up a string by dividing the num by 4 and taking the remainder each time.
    """
    result = ""

    for _ in range(length):
        curr_base = base(num % 4)
        result = curr_base + result
        num = num/4

    return result

cached_similar_kmers = {}

def make_all_permutations_of_kmer(kmer, d):
    if d == 0:
        return [kmer]

    cache_key = kmer + str(d)
    if cache_key not in cached_similar_kmers:
        result = []
        temp = find_all_single_permutations(kmer)
        for permuted in temp:
                result += make_all_permutations_of_kmer(permuted, d-1)
        cached_similar_kmers[cache_key] = result

    return cached_similar_kmers[cache_key]


def find_all_single_permutations(seq):
    result = [] # start off with seq itself
    for i in range(len(seq)):
        result += permute_single_letter(seq, i)
    return result


def permute_single_letter(seq, i):
    result = []
    for b in ['A', 'C', 'G', 'T']:
        if seq[i] != b:
            temp = seq[:i] + b + seq[i+1:]
            result += [temp]

    return result


def build_empty_kmer_cache(k):
    cache = {}
    for i in xrange(4**k):
        cache[int_to_sequence(i, k)] = 0

    return cache


def find_kmers_using_prebuilt_cache(kmers, sequence, k):
    for i in xrange(len(sequence) - k + 1):
        kmers[sequence[i: i + k]] += 1

    return kmers


def find_exact_kmers(sequence, k):
    kmers = {}
    for i in xrange(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        if current_kmer in kmers:
            kmers[current_kmer] += 1
        else:
            kmers[current_kmer] = 1

    return kmers


def find_kmers_with_mismatches(sequence, k , d):
    kmers = {}
    for i in xrange(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        kmer_and_mismatches = set([current_kmer] + make_all_permutations_of_kmer(current_kmer, d))

        for kmer in kmer_and_mismatches:
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1

    return kmers


def find_freq_words_with_mismatches_and_reverse_compliments(sequence, k , d):
    kmers = {}
    for i in xrange(len(sequence) - k + 1):
        current_kmer = sequence[i: i + k]
        kmer_and_mismatches = set([current_kmer] + make_all_permutations_of_kmer(current_kmer, d))
        reverse_kmers = set([reverse_compliment(current_kmer)] + make_all_permutations_of_kmer(reverse_compliment(current_kmer), d))

        for kmer in kmer_and_mismatches:
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1


        for kmer in reverse_kmers:
            #kmer = reverse_compliment(rkmer)
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1




    return kmers

def reverse_compliment(seq):

    rev = seq[::-1].lower()

    # now convert a -> T, t -> A, c -> G, g -> C
    revc = rev.replace('a', 'T').replace('t', 'A').replace('c', 'G').replace('g', 'C')

    return revc

def is_approx_match(pattern, sequence, tolerance):
    if len(pattern) != len(sequence):
        return False

    mismatch_count = 0
    for a, b in zip(pattern, sequence):
        if a != b:
            mismatch_count += 1
            if mismatch_count > tolerance:
                return False

    return True


def compute_kmers_slowly(seq, k):
    """
    :param seq: A sequence af ACGTs
    :param k: Length of kmer
    :return: An of kmers counts, indexes in the array are the kmer integer representations.
    """

    # size of array is max poss integer value which is length*4 - 1
    kmers = {}

    for i in range(len(seq) - k + 1):
        kmer = seq[i: i + k]
        numeric_value = sequence_to_int(kmer)
        if kmers.has_key(numeric_value):
            kmers[numeric_value] += 1
        else:
            kmers[numeric_value] = 1

    return kmers


def compute_kmers_slowly2(seq, k):
    """
    :param seq: A sequence af ACGTs
    :param k: Length of kmer
    :return: An of kmers counts, indexes in the array are the kmer integer representations.
    """

    max_power = 4 ** (k-1)
    kmers = {}
    first_kmer = seq[0:k]
    numeric_value = sequence_to_int(first_kmer)
    kmers[numeric_value] = 1

    for i in xrange(k, len(seq)):
        new_val = int_value(seq[i])

        # shift the kmer up numerically...
        # knock of the most significant base from index, multiply by 4 and add the new value
        numeric_value = numeric_value % max_power
        numeric_value = numeric_value * 4
        numeric_value += new_val

        if kmers.has_key(numeric_value):
            kmers[numeric_value] += 1
        else:
            kmers[numeric_value] = 1

    return kmers
