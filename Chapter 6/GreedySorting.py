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

    p = "(+20 +7 +10 +9 +11 +13 +18 -8 -6 -14 +2 -4 -16 +15 +1 +17 +12 -5 +3 -19)"
    p = list(map(int, p.lstrip('(').rstrip(')').split()))

    result = greedy_sort(p)

    for r in result:
        print(r)

    print(len(result))

    formatted_output_list = ['('+' '.join([['', '+'][i > 0] + str(i) for i in permutation])+')' for permutation in result]


    with open('greedy_sorted.txt', 'w') as file:
        file.write('\n'.join(formatted_output_list))


if __name__ == "__main__":
    sys.exit(main())