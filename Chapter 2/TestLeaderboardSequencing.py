import unittest

import LeaderboardCyclopeptideSequencing as lb


class TestLeaderboardSequencing(unittest.TestCase):
    def test_trim_1(self):
        spectrum = [0, 57, 138, 227]

        leaders = [[57, 71, 87], [57, 71, 99], [57, 71, 97]]

        result = lb.trim(leaders, spectrum, 3)
        self.assertListEqual(leaders, result)

        result = lb.trim(leaders, spectrum, 2)
        self.assertEqual(len(leaders), len(result))

        result = lb.trim(leaders, spectrum, 1)
        self.assertListEqual(result[0], [57, 71, 99])

    def test_seq_1(self):
        spectrum = [0, 57, 138, 227]
        all_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
        result = lb.leaderboard_sequence(spectrum, 3, all_masses)

        self.assertIsNotNone(result)

        # ##self.assertEquals(len(result), 3)

    def test_seq_exercise(self):
        all_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

        result = lb.leaderboard_sequence([0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460], 10, all_masses)
        self.assertIsNotNone(result)

        # ##self.assertEquals(len(result), 4)

    def test_alphabet_builder(self):
        result = lb.build_alphabet([0, 50, 100, 150, 200, 250], 2)

        self.assertIsNotNone(result)


    def test_cyc_score(self):
        r1 = lb.lin_score([99, 71, 137, 57, 72, 57],
                          [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394,
                           422, 493])
        r2 = lb.lin_score([71, 99, 129, 57, 57, 80],
                          [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394,
                           422, 493])

        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()