"""
    File: TestFreqWordsWithMismatches.py
    Author: steve
    Created: 10/08/2014
    
"""
import unittest

import BranchAndBound as BandB


class TestBranchAndBound(unittest.TestCase):
    def test_quiz(self):
        peps = ["QCV", "AQV", "AVQ", "TVQ", "VAQ", "ETC"]
        integer_mass = dict(G=57, A=71, S=87, P=97, V=99, T=101, C=103, I=113, L=113, N=114, D=115, K=128, Q=128, E=129,
                            M=131, H=137, F=147, R=156, Y=163, W=186)

        for pep in peps:
            pep_as_ints = []
            for p in pep:
                pep_as_ints.append(integer_mass[p])

            lin_spec = BandB.linear_spectrum(pep_as_ints)
            exp = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333]
            ok = True
            for t in lin_spec:
                if t in exp:
                    exp.remove(t)
                else:
                    ok = False
                    break

            print(pep, ok)


    def test_consistent_empty_values(self):
        self.assertTrue(BandB.is_consistent([], []), "Empty values not consistent.")

    def test_consistent_single_values(self):
        a_zero = [0]
        self.assertTrue(BandB.is_consistent(a_zero, a_zero), "Two zero values not consistent.")

    def test_consistent_several_identical_values(self):
        some_values = [0, 128, 128]
        some_more_values = [0, 128, 128, 256]
        self.assertTrue(BandB.is_consistent(some_values, some_more_values), "Two identical values not consistent.")

    def test_consistent_larger_experimental_list(self):
        exp = [0, 77, 128, 128, 233, 233, 233, 233, 1000, 10384848]
        theory = [0, 77, 128, 233, 1000, 233, 233]
        self.assertTrue(BandB.is_consistent(theory, exp), "Two consistent values not consistent.")

    def test_not_consistent_zero_experimental(self):
        self.assertFalse(BandB.is_consistent([0, 123], [99]), "Inconsistent values found to be consistent.")

    def test_not_consistent_too_many_theoretical(self):
        self.assertFalse(BandB.is_consistent([0, 123, 123], [0, 123]), "Inconsistent values found to be consistent.")

    def test_not_consistent_mismatch(self):
        self.assertFalse(BandB.is_consistent([0, 123, 123, 456], [0, 124, 123, 456]),
                         "Inconsistent values found to be consistent.")


    def test_expand(self):
        expanded = BandB.expand([[0]])
        self.assertEquals(len(BandB.all_masses), len(expanded), "Unexpected number of expansion results")

    def test_expand2(self):
        expanded = BandB.expand([[0]])
        self.assertEquals(2, len(expanded[2]), "Unexpected size of expansion result.")

    def test_cyclo_spectrum_single_matching(self):
        self.assertListEqual([0, 71], BandB.cyclo_spectrum([71]))

    def test_cyclo_sequencing_single_item(self):
        cyclo_sequence = BandB.cyclopeptide_sequencing([0, 99])
        self.assertEquals(cyclo_sequence, [[99]])

    def test_cyclo_sequencing_two_items(self):
        cyclo_sequence = BandB.cyclopeptide_sequencing([0, 57, 71, 128])
        self.assertTrue([57, 71] in cyclo_sequence)
        self.assertTrue([71, 57] in cyclo_sequence)

    def test_cyclo_sequenceing_tetbook_example(self):
        cyclo_sequence = BandB.cyclopeptide_sequencing([0, 113, 128, 186, 241, 299, 314, 427])
        self.assertTrue([186, 128, 113] in cyclo_sequence)
        self.assertTrue([186, 113, 128] in cyclo_sequence)
        self.assertTrue([128, 186, 113] in cyclo_sequence)
        self.assertTrue([128, 113, 186] in cyclo_sequence)
        self.assertTrue([113, 186, 128] in cyclo_sequence)


if __name__ == "__main__":
    unittest.main()