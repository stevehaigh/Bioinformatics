from builtins import range, dict

__author__ = 'steve'

import unittest
import GibbsSampler as gs
import RandomisedMotifSearch as rms


class MyTestCase(unittest.TestCase):
    def test_random(self):
        pdf = [0.1, 0.8, 0.1]

        results = dict()

        for _ in range(0, 100000):
            i = gs.biased_random_selector(pdf)
            if i in results:
                results[i] += 1
            else:
                results[i] = 1

        print(results)

    def test_random_most_probable_kmer_for_profile(self):

        p = rms.create_profile(["CAAAA", "AGAAC", "ATAAA", "GAACG"])
        s = "ATATA"
        k = 3

        for i in range(0, 100):
            result = gs.random_most_probable_kmer_for_profile(p, s, k)
            print (result)


if __name__ == '__main__':
    unittest.main()
