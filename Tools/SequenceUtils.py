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


def compute_kmers_slowly(seq, length):
    """
    :param seq: A sequence af ACGTs
    :param length: Length of kmer
    :return: An of kmers counts, indexes in the array are the kmer integer representations.
    """

    # size of array is max poss integer value which is length*4 - 1
    kmers = {}

    for i in range(len(seq) - length + 1):
        kmer = seq[i: i + length]
        index = sequence_to_int(kmer)
        if kmers.has_key(index):
            kmers[index] += 1
        else:
            kmers[index] = 1

    return kmers


def compute_kmers_fast(seq, length):
    """
    :param seq: A sequence af ACGTs
    :param length: Length of kmer
    :return: An of kmers counts, indexes in the array are the kmer integer representations.
    """

    max_power = 4 ** (length-1)
    kmers = {}
    first_kmer = seq[0:length]
    index = sequence_to_int(first_kmer)
    kmers[index] = 1

    for i in xrange(length, len(seq)):
        new_val = int_value(seq[i])

        # shift the kmer up numerically...
        # knock of the most significant base from index, multiply by 4 and add the new value
        debug = int_to_sequence(index, length)

        index = index % max_power
        debug = int_to_sequence(index, length)

        index = index * 4
        debug = int_to_sequence(index, length)

        index += new_val
        debug = int_to_sequence(index, length)

        if kmers.has_key(index):
            kmers[index] += 1
        else:
            kmers[index] = 1

    return kmers
