"""
    File: LeaderboardCyclopeptideSequencing
    Author: steve
    Created: 14/11/14
    
"""
import sys
import operator
import time
from builtins import range, len, sorted, max, sum, dict, list, map, int, str


_all_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def expand(peptides, alphabet):
    expanded = []
    for p in peptides:
        for m in alphabet:
            new_p = p + [m]
            expanded.append(new_p)

    return expanded


def linear_spectrum(peptide):
    """
    :param peptide: string representation of a peptide
    :return: integer linear spectrum as a list of int
    """

    prefix_mass = [0]

    for i in range(0, len(peptide)):
        prefix_mass.append(prefix_mass[i] + peptide[i])

    linear_spectrum = []
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    return sorted(linear_spectrum)


def cyclic_spectrum(peptide):
    """
    :param peptide: string representation of a peptide
    :return: integer cyclic spectrum as a list of int
    """

    prefix_mass = [0]

    for i in range(0, len(peptide)):
        prefix_mass.append(prefix_mass[i] + peptide[i])

    peptide_mass = prefix_mass[len(peptide)]

    cyclic_spectrum = []
    for i in range(0, len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            # do wrap arounds
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))

    return sorted(cyclic_spectrum)


def cyc_score(peptide, spectrum):
    score = 0
    cyc_spectrum = cyclic_spectrum(peptide)
    spectrum_copy = spectrum[:]

    for c in cyc_spectrum:
        if c in spectrum_copy:
            score += 1
            spectrum_copy.remove(c)

    return score


def lin_score(peptide, spectrum):
    score = 0
    lin_spectrum = linear_spectrum(peptide)
    spectrum_copy = spectrum[:]

    for c in lin_spectrum:
        if c in spectrum_copy:
            score += 1
            spectrum_copy.remove(c)

    return score


def trim(leader_board, spectrum, n):
    if len(leader_board) > n:
        leader_scores = []
        for peptide in leader_board:
            leader_scores.append((lin_score(peptide, spectrum), peptide))

        leader_scores = sorted(leader_scores, key=operator.itemgetter(0), reverse=True)
        nth_score = leader_scores[n - 1][0]

        temp = []
        for i in range(0, len(leader_scores)):
            if leader_scores[i][0] >= nth_score:
                temp.append(leader_scores[i][1])

        leader_board = temp

    return leader_board


def leaderboard_sequence(spectrum, n, alphabet):
    spectrum = sorted(spectrum)
    parent_mass = max(spectrum)
    leader_board = [[]]
    leader_peptide = []

    while len(leader_board) > 0:
        leader_board = expand(leader_board, alphabet)
        # copy for loop
        # leader_score = score(leader_peptide, spectrum)
        leader_score = 0
        temp = leader_board[:]
        for peptide in temp:
            mass = sum(peptide)
            if mass == parent_mass:
                s = cyc_score(peptide, spectrum)
                if s > leader_score:
                    leader_peptide = peptide
                    leader_score = s

            elif mass > parent_mass:
                leader_board.remove(peptide)

        leader_board = trim(leader_board, spectrum, n)

    return leader_peptide


def build_alphabet(spectrum, m):
    """

    :param spectrum: an experimental spectrum
    :param m: the multiplicity threshold
    :return: a convolution spectrum, trimmed to contain only peptide masses appearing m times or more.
    """

    convolutions = dict()

    for i in range(0, len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            diff = spectrum[j] - spectrum[i]
            if diff > 0 and 57 <= diff <= 200:
                if diff in convolutions.keys():
                    convolutions[diff] += 1
                else:
                    convolutions[diff] = 1

    sorted_list = sorted(convolutions.items(), key=operator.itemgetter(1), reverse=True)

    score_to_beat = sorted_list[m - 1][1]

    result = []

    for item in sorted_list:
        if item[1] >= score_to_beat:
            result.append(item[0])

    return result


def convolution_cyclopeptide_sequencing(spectrum, m, n):
    """

    :param spectrum: the experimental spectrum
    :param n: the leader board trim size
    :param m: the convolution spectrum frquency cut-off
    :return: the peptide!
    """
    alphabet = build_alphabet(spectrum, m)
    return leaderboard_sequence(spectrum, n, alphabet)


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # data = "0 71 87 99 99 99 101 103 113 114 115 128 128 128 129 129 147 147 163 163 163 172 199 202 216 216 228 228 241 243 243 246 256 261 262 262 264 277 300 310 310 315 315 315 327 331 335 344 345 356 371 371 376 391 409 409 409 411 418 424 424 428 442 443 444 444 444 459 463 478 482 484 499 510 523 523 523 531 538 543 543 547 558 570 572 572 581 587 587 591 607 610 612 625 646 652 659 660 670 671 673 683 686 686 686 686 687 706 706 709 715 738 739 744 754 759 774 784 785 786 787 788 809 814 815 815 833 833 834 837 853 853 858 868 872 885 887 887 902 902 903 914 922 932 934 943 947 952 956 967 981 986 986 996 1000 1001 1002 1005 1014 1030 1031 1031 1050 1050 1061 1069 1070 1080 1094 1095 1097 1101 1114 1115 1115 1130 1130 1130 1133 1148 1149 1159 1165 1168 1183 1193 1196 1197 1197 1202 1224 1229 1229 1230 1233 1243 1258 1261 1267 1277 1278 1293 1296 1296 1296 1311 1311 1312 1325 1329 1331 1332 1346 1356 1357 1365 1376 1376 1395 1395 1396 1412 1421 1424 1425 1426 1430 1440 1440 1445 1459 1470 1474 1479 1483 1492 1494 1504 1512 1523 1524 1524 1539 1539 1541 1554 1558 1568 1573 1573 1589 1592 1593 1593 1611 1611 1612 1617 1638 1639 1640 1641 1642 1652 1667 1672 1682 1687 1688 1711 1717 1720 1720 1739 1740 1740 1740 1740 1743 1753 1755 1756 1766 1767 1774 1780 1801 1814 1816 1819 1835 1839 1839 1845 1854 1854 1856 1868 1879 1883 1883 1888 1895 1903 1903 1903 1916 1927 1942 1944 1948 1963 1967 1982 1982 1982 1983 1984 1998 2002 2002 2008 2015 2017 2017 2017 2035 2050 2055 2055 2070 2081 2082 2091 2095 2099 2111 2111 2111 2116 2116 2126 2149 2162 2164 2164 2165 2170 2180 2183 2183 2185 2198 2198 2210 2210 2210 2224 2227 2254 2263 2263 2263 2279 2279 2297 2297 2298 2298 2298 2311 2312 2313 2323 2325 2327 2327 2327 2339 2355 2426"
    # n = 358
    # data_as_list = list(map(int, data.split(' ')))
    #
    # result = leaderboard_sequence(data_as_list, n, _all_masses)



    data = "114 1199 245 1312 358 128 356 922 702 709 1184 1053 959 373 959 724 1087 587 603 131 0 1298 472 1184 840 595 356 1289 128 131 99 845 1058 230 1070 586 583 1426 455 114 1068 700 817 484 1062 472 344 368 686 1167 227 1295 99 1327 475 341 364 1198 823 1295 1181 831 726 1070 1181 467 504 1186 598 228 839 345 259 240 1196 828 495 1312 954 843 712 1190 840 242 823 1085 114 1327 942 717 358 609 695 245 482 823 603 1068 1050 967 586 1298 472 581 242 1298 944 740 231 951 931 376 1199 596 128 1195 103 954 714 467 830 1082 137 236 339 1312 971 731 954 459 603 1323 227 1081"
    m = 16
    n = 330

    start = time.clock()

    data_as_list = list(map(int, data.split(' ')))
    result = convolution_cyclopeptide_sequencing(data_as_list, m, n)

    end = time.clock()

    print(end - start)

    print ("-".join(map(str, result)))


if __name__ == "__main__":
    sys.exit(main())