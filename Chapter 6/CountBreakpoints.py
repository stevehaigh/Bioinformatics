"""
    File: CountBreakpoints
    Author: steve
    Created: 05/01/15
    
"""
import sys


def count_breakpoints(seq):
    """
    Counts the number of breakpoints by checking for any point where list is not increasing by 1
    :param seq:
    :return:
    """

    seq = [0] + seq[:] + [len(seq) + 1]
    count = 0

    for i in range(0, len(seq) - 1):
        if seq[i + 1] - seq[i] != 1:
            count += 1

    return count

def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    seq = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
    seq_as_list = list(map(int, seq.lstrip('(').rstrip(')').split()))
    print (count_breakpoints(seq_as_list))


if __name__ == "__main__":
    sys.exit(main())