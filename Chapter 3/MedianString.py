"""
    File: MedianString
    Author: steve
    Created: 20/11/14
    
"""
from builtins import zip, enumerate, len, Exception, range, min, sum, sorted
from os2emxpath import sep
import sys


def hamming_distance(pattern1, pattern2):
    if len(pattern1) != len(pattern2):
        raise Exception("Pattern lengths must match to get Hamming distance.")

    count = 0
    for i, (char1, char2) in enumerate(zip(pattern1, pattern2)):
        if char1 != char2:
            count += 1

    return count


def minimum_distance(pattern, dna):
    """
    Finds the minimum distance between a pattern and dna.
    :param pattern:
    :param dna:
    :return:
    """
    if len(pattern) > len(dna):
        raise Exception("Can't look for a pattern in {0} as it is smaller than the {1}".format(dna, pattern))

    k = len(pattern)
    min_distance = sys.maxsize

    for i in range(0, len(dna) - k + 1):
        min_distance = min(min_distance, hamming_distance(pattern, dna[i:i + k]))

    if min_distance == sys.maxsize:
        raise Exception(
            "It appears there was a problem calculating the minimum distance between {0} and {1}".format(dna, pattern))

    return min_distance


def DistanceBetweenPatternAndStrings(pattern, dna):
    """
    total_distance ← 0
    for each string text in Dna
        get the min_distance for text
        distance ← distance + min_distance
    return distance

    :param Pattern: a potential motif patter
    :param Dna: an array of DNA strings
    :return: the cumulative count of differences
    """
    return sum(minimum_distance(pattern, text) for text in dna)


def build_all_kmers(k):
    if k == 0:
        return [""]

    sub_list = build_all_kmers(k - 1)
    result = []
    for kmer in sub_list:
        result.append(kmer + "A")
        result.append(kmer + "C")
        result.append(kmer + "G")
        result.append(kmer + "T")

    return result


def MedianString(dna, k):
    """
    MEDIANSTRING(Dna, k)
        distance ← ∞
        for each k-mer Pattern from AA…AA to TT…TT
            if distance > d(Pattern, Dna)
                 distance ← d(Pattern, Dna)
                 Median ← Pattern
        return Median
    :param dna:
    :param k:
    :return:
    """

    distance = sys.maxsize
    median = ""
    medians = []

    for kmer in build_all_kmers(k):
        d = DistanceBetweenPatternAndStrings(kmer, dna)
        if d < distance:
            distance = d
            median = kmer
            medians = [kmer]
        elif d == distance:
            medians.append(kmer)

    print("debug")
    medians = sorted(medians)
    print(*medians, sep='\n')

    return median


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv


if __name__ == "__main__":
    sys.exit(main())