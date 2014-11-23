"""
    File: ProfileMostProbableKmer
    Author: steve
    Created: 22/11/14
    
"""
from builtins import dict, list, map, float, range, len
import sys


def build_probability_matrix(probs_as_strings):
    """
    Build the matrix
    :param probs_as_strings:
    :return:
    """

    matrix = dict()

    matrix['A'] = list(map(float, probs_as_strings[0].split(' ')))
    matrix['C'] = list(map(float, probs_as_strings[1].split(' ')))
    matrix['G'] = list(map(float, probs_as_strings[2].split(' ')))
    matrix['T'] = list(map(float, probs_as_strings[3].split(' ')))

    return matrix


def get_probability_of_kmer(kmer, matrix):
    cumulative_product = 1
    for i in range(0, len(kmer)):
        cumulative_product *= matrix[kmer[i]][i]

    return cumulative_product


def find_most_probable_kmer(l, dna, matrix):
    most_probable_kmer = ""
    max_probability = 0

    for i in range(0, len(dna) - l + 1):
        kmer = dna[i:i + l]
        score = get_probability_of_kmer(kmer, matrix)
        if score > max_probability:
            max_probability = score
            most_probable_kmer = kmer

    return most_probable_kmer


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    dna = "CCCTTCCGTCTCTGTGACACCCTTATGCTTCGCTCAAATGTAACCCTGCATCGAGCTCGCCCGCAGCGAAGACAGCCGCACGTGCTGTGGAATCAAAGAATCGACTGGTAAGCTTGGGTCAGGCGAATTGTACTTAGTCAAGAGTTGAACGTCTGATTCGACTTGCTCCACATCCCCGAGCTGTGACACCTTACCAGATCTACGTGCGAGCCCATGGCTTGCTCGGGACGCGAACCCTAAACTAGTTGCACTCAATCTCGGGCGCTGAAATCTGCCGCCACTCCTCAGCGGCAGACCTGCAGCGAATTCTAGCTGGCCAATCTCTGGTAACACCCACCCGAGCAAAGATACTCGCTGGATCCGCTTGTCAAGAGCCTTAGTAGGGTGTCCCTACAATCCAATCCTAAAGTTATATGCGGCCACCCTCGATTGTCTCTCGGCCCGTCTGTTATCAAGATAGGCACAGTGAAATTTCGCCCCGCCATGGCATGTGTCCTGTTGAATTCAACGGAGACCATACTAAAAGTCTGAACCAGTTTAGTAAAAACCTGCATTGACCGTCTTTCATAGTTGCCGTTAGCGCGGTCTGCAAGGGCGACTTAATCATTCTTCGTACGCGTATACGTGATTATTCCGTACTCTACCGGTGTTGTCCAAGCTCATATAATCGCCTACGACCATACGGTTTTCTAGTTGTAGGAAAAGTTACACATCGTCAGACAACGTCAGGGGAGGTTAGAGCATGGAACTGTAGGGCTACCCCTGGGCTCCTTTGGACATCCACCTGGGGTATTCAAGCCGTCGAAAGATCCTTCGACCCGTATCGCCGGGTGTACGACGCATCCCTCCTTTTCACGGTCCGCGCAAACACAATAGCGGGAAAAATGGCGATAGGTCACAGTGCAACGAGTCGGACGTCGTCCGAGTCTTTCTCAGTTCCGCTCAACAGTAAGTATAATCGTACCACGCTCCTGGATTACCTGATTTGGGATGAAAGGTG"
    length = 15

    data_probs = ["0.136 0.212 0.258 0.258 0.212 0.288 0.258 0.273 0.364 0.167 0.288 0.273 0.303 0.288 0.242", \
                  "0.318 0.212 0.273 0.182 0.258 0.258 0.242 0.227 0.227 0.333 0.288 0.242 0.258 0.258 0.303", \
                  "0.318 0.273 0.227 0.303 0.288 0.258 0.288 0.242 0.167 0.333 0.152 0.273 0.212 0.212 0.227", \
                  "0.227 0.303 0.242 0.258 0.242 0.197 0.212 0.258 0.242 0.167 0.273 0.212 0.227 0.242 0.227"]

    matrix = build_probability_matrix(data_probs)

    print(find_most_probable_kmer(length, dna, matrix))

    matrix = build_probability_matrix(data_probs)


if __name__ == "__main__":
    sys.exit(main())