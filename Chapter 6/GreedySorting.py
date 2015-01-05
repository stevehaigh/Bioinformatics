"""
    File: GreedySorting
    Author: steve
    Created: 05/01/15
    
"""

# Lambda function to find the index of a given element in the permutation.
from operator import neg
from pprint import pprint
import sys

def apply_reversal(permutation, i, j):
    """
    reverses a slice from i to j, negating each element in the slice
    """

    swap_section = list(map(neg, reversed(permutation[i:j+1])))
    return permutation[:i] + swap_section + permutation[j+1:]


def greedy_sort(permutation):
    """
    GREEDYSORTING(P)
        approxReversalDistance ← 0
        for k = 1 to |P|
            if element k is not sorted
                apply the k-sorting reversal to P
                approxReversalDistance ← approxReversalDistance + 1
            if k-th element of P is −k
                apply the k-sorting reversal to P
                approxReversalDistance ← approxReversalDistance + 1
        return approxReversalDistance
    :param p:
    :return:
    """

    permutations = []
    i = 0
    while i < len(permutation):
        if permutation[i] == i+1:
            i += 1
        else:
            j = list(map(abs, permutation)).index(i+1)
            permutation = apply_reversal(permutation, i, j)
            permutations.append(permutation)

    return permutations


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    p =  "(-18 -65 -105 -55 -93 -59 +7 -106 +75 -88 +118 +29 +9 -12 -33 -61 +56 +27 +54 +108 -21 +47 +119 -45 +104 -120 +30 +83 +25 +69 +70 +115 +52 -100 -13 -8 -58 +103 -101 -63 +68 -77 +97 -86 -85 -74 -121 -92 -116 +16 +3 -91 -49 +39 -44 -71 -51 -113 -32 +60 -81 -87 -22 -37 +43 +76 +99 +50 -48 +62 +111 -20 +26 -80 -38 +35 +110 -64 +53 -14 -2 +96 +46 -73 -31 +36 +112 +90 -17 -41 +117 -109 -89 -84 -95 +72 +5 -28 -102 -23 -79 -24 +114 -19 -107 +10 +42 -15 -67 +6 +57 +40 +98 +78 +1 +66 -4 -11 -82 -34 -94)"
    p = list(map(int, p.lstrip('(').rstrip(')').split()))

    result = greedy_sort(p)

    for r in result:
        print(r)

    formatted_output_list = ['('+' '.join([['', '+'][i > 0] + str(i) for i in permutation])+')' for permutation in result]


    with open('greedy_sorted.txt', 'w') as file:
        file.write('\n'.join(formatted_output_list))


if __name__ == "__main__":
    sys.exit(main())