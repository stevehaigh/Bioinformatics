"""
    File: TestFreqWordsWithMismatches.py
    Author: steve
    Created: 10/08/2014
    
"""
import unittest
import FreqWordsWithMismatches as fwwmm


class TestSequenceFunctions(unittest.TestCase):
    def test_all_as(self):
        result = fwwmm.find_freq_words_with_mismatches("AAAA", 2, 0)
        self.assertEqual(len(result), 1)
        result = fwwmm.find_freq_words_with_mismatches("AAAA", 2, 1)
        self.assertEqual(len(result), 7)


    def test_aabb(self):
        result = fwwmm.find_freq_words_with_mismatches("AAGG", 2, 0)
        self.assertEqual(len(result), 3)


    def test_data_from_example(self):
        result = fwwmm.find_freq_words_with_mismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()