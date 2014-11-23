"""
    File: TestProfileMostProbableKmer
    Author: steve
    Created: 22/11/14
    
"""
import unittest

import ProfileMostProbableKmer as pmpk


class TestProfileMostProbableKmer(unittest.TestCase):
    def test_build_probability_matrix(self):
        result = pmpk.build_probability_matrix(
            ["0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4"])
        self.assertEqual(result['A'], [0.1, 0.2, 0.3, 0.4])


    def test_get_prob(self):
        matrix = pmpk.build_probability_matrix(
            ["0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.4"])
        result = pmpk.get_probability_of_kmer("ACGT", matrix)

        self.assertEqual(result, 0.1 * 0.2 * 0.3 * 0.4)


    def test_from_book(self):
        dna = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
        length = 5

        data_probs = ["0.2 0.2 0.3 0.2 0.3",
                      "0.4 0.3 0.1 0.5 0.1",
                      "0.3 0.3 0.5 0.2 0.4",
                      "0.1 0.2 0.1 0.1 0.2"]

        matrix = pmpk.build_probability_matrix(data_probs)

        result = pmpk.find_most_probable_kmer(length, dna, matrix)

        self.assertEqual(result, "CCGAG")

