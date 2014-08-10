"""
    File: TestSequenceUtils
    Author: steve
    Created: 09/08/2014
"""
import unittest
import SequenceUtils

class TestSequenceFunctions(unittest.TestCase):

    def test_seq_to_int_with_empty_seq(self):
        result = SequenceUtils.sequence_to_int("")
        self.assertEqual(result, 0)


    def test_seq_to_int_all_a(self):
        result = SequenceUtils.sequence_to_int("AAAA")
        self.assertEqual(result, 0)


    def test_seq_to_int_all_c(self):
        result = SequenceUtils.sequence_to_int("CCCC")
        # expect result to be 1+4+16+64
        self.assertEqual(result, 85)


    def test_seq_to_int_all_g(self):
        result = SequenceUtils.sequence_to_int("GGGG")
        # expect result to be 2 * 1+4+16+64
        self.assertEqual(result, 170)


    def test_seq_to_int_all_t(self):
        result = SequenceUtils.sequence_to_int("TTTT")
        # expect result to be 3 * 1+4+16+64
        self.assertEqual(result, 255)


    def test_seq_to_int_one_of_each(self):
        result = SequenceUtils.sequence_to_int("ACGT")
        # expect result to be 0*64 + 1*16 +  2*4 + 3
        self.assertEqual(result, 27)


    def test_seq_to_int_one_of_each_reversed(self):
        result = SequenceUtils.sequence_to_int("TGCA")
        # expect result to be 3*64 + 2*16 + 1*4 + 0
        self.assertEqual(result, 228)


    def test_seq_to_int_longer(self):
        result = SequenceUtils.sequence_to_int("CGTATTGATTCCCGATAGT")
        self.assertEqual(result, 117008324811)

    def test_seq_to_int_error(self):
        self.assertRaises(ValueError, SequenceUtils.sequence_to_int, "ACGTBCGTA")


    def test_int_to_seq_with_zero_number(self):
        result = SequenceUtils.int_to_sequence(0,0)
        self.assertEqual(result, "")


    def test_int_to_seq_all_a(self):
        result = SequenceUtils.int_to_sequence(0, 4)
        self.assertEqual(result, "AAAA")

    def test_int_to_seq_all_c(self):
        result = SequenceUtils.int_to_sequence(85, 4)
        # expect result to be 1+4+16+64
        self.assertEqual(result, "CCCC")


    def test_int_to_seq_all_g(self):
        result = SequenceUtils.int_to_sequence(170, 4)
        # expect result to be 2 * 1+4+16+64
        self.assertEqual(result, "GGGG")


    def test_int_to_seq_all_t(self):
        result = SequenceUtils.int_to_sequence(255, 4)
        # expect result to be 3 * 1+4+16+64
        self.assertEqual(result, "TTTT")


    def test_int_to_seq_one_of_each(self):
        result = SequenceUtils.int_to_sequence(27, 4)
        # expect result to be 0*64 + 1*16 +  2*4 + 3
        self.assertEqual(result, "ACGT")


    def test_int_to_seq_one_of_each_reversed(self):
        result = SequenceUtils.int_to_sequence(228, 4)
        # expect result to be 3*64 + 2*16 + 1*4 + 0
        self.assertEqual(result, "TGCA")


    def test_int_to_seq_longer(self):
        result = SequenceUtils.int_to_sequence(117008324811, 19)
        self.assertEqual(result, "CGTATTGATTCCCGATAGT")


    def test_compute_kmers_simple_1(self):
        result = SequenceUtils.find_exact_kmers("AAAA", 2)
        self.assertEqual(len(result), 1)


    def test_compute_kmers_simple_2(self):
        result = SequenceUtils.find_exact_kmers("AACC", 2)
        self.assertEqual(len(result), 3)


    def test_reverse_compliment_acgt(self):
        result = SequenceUtils.reverse_compliment("ACGT")
        self.assertEqual(result, "ACGT")


    def test_reverse_compliment_aaaa(self):
        result = SequenceUtils.reverse_compliment("AAAA")
        self.assertEqual(result, "TTTT")


    def test_reverse_compliment_cccc(self):
        result = SequenceUtils.reverse_compliment("CCCC")
        self.assertEqual(result, "GGGG")


    def test_reverse_compliment_ggaa(self):
        result = SequenceUtils.reverse_compliment("GGAA")
        self.assertEqual(result, "TTCC")


    def test_reverse_compliment_ggttcc(self):
        result = SequenceUtils.reverse_compliment("GGTTCC")
        self.assertEqual(result, "GGAACC")


    def test_permute_single_letter(self):
        result = SequenceUtils.permute_single_letter("AAAA", 0)
        self.assertEqual(len(result), 3)


    def test_find_all_single_permutations(self):
        result = SequenceUtils.find_all_single_permutations("AAAA")
        self.assertEqual(len(result), 12)


    def test_find_d_permutations_of_seq(self):
        result = SequenceUtils.make_all_permutations_of_kmer("AAAA", 0)
        self.assertEqual(len(result), 1)
        result = SequenceUtils.make_all_permutations_of_kmer("AAAA", 1)
        self.assertEqual(len(result), 12)
        result = SequenceUtils.make_all_permutations_of_kmer("AAAA", 2)
        self.assertEqual(len(result), 144)


    def test_build_empty_cache(self):
        result = SequenceUtils.build_empty_kmer_cache(1)
        self.assertEqual(len(result), 4)
        result = SequenceUtils.build_empty_kmer_cache(2)
        self.assertEqual(len(result), 16)


if __name__ == '__main__':
    unittest.main()