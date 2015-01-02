"""
    File: LCS
    Author: steve
    Created: 30/12/14

    ALERT!!! This is BUGGY, use GlobalAlignment.py instead!!!
    
"""
from pprint import pprint
import sys


def lcs_backtrack(v, w):
    """
    Finds the LCS backtrack matrix for two strings, v and w
    ALERT!!! This is BUGGY, use GlobalAlignment.py instead!!!
    """

    s = [x[:] for x in [[0]*(len(w))]*(len(v))]
    backtrack = [x[:] for x in [[0]*(len(w))]*(len(v))]

    for i in range(1, len(v)):
        for j in range(1, len(w)):
            if v[i] == w[j]:
                s[i][j] = s[i-1][j-1] + 1
                backtrack[i][j] = '#'
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1])

                if s[i][j] == s[i-1][j]:
                    backtrack[i][j] = 'd'
                elif s[i][j] == s[i][j-1]:
                    backtrack[i][j] = 'a'

    return backtrack


def output_lcs(backtrack, v, i, j):
    result = ""

    while i >= 0:
        if backtrack[i][j] == 'd':
            i = i - 1
        elif backtrack[i][j] == 'a':
            j = j - 1
        elif backtrack[i][j] == '#':
            result = v[i] + result
            i = i - 1
            j = j - 1
        else:
            print("!")
            i = i - 1
            j = j - 1

    return(result)

def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    ALERT!!! This is BUGGY, use GlobalAlignment.py instead!!!
    """
    if argv is None:
        argv = sys.argv

    v = "TGTACG"
    w = "GCTAGT"

    b = lcs_backtrack(v, w)

    r = output_lcs(b, v, len(v)-1, len(w)-1)

    print(r)
    print("ALERT!!! This is BUGGY, use GlobalAlignment.py instead!!!")


if __name__ == "__main__":
    main()
    #sys.exit(main())