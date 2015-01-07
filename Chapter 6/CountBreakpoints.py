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

    seq = "(-16 -20 +11 +12 -14 -13 -15 -6 -8 -19 -18 -17 -10 +4 -5 -2 +7 -3 +1 -9)"
    seq_as_list = list(map(int, seq.lstrip('(').rstrip(')').split()))
    print (count_breakpoints(seq_as_list))


if __name__ == "__main__":
    sys.exit(main())