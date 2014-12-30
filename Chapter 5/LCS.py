"""
    File: LCS
    Author: steve
    Created: 30/12/14
    
"""
from pprint import pprint
import sys


def lcs_backtrack(v, w):
    """
    Finds the LCS backtrack matrix for two strings, v and w

    ....
    for i ← 0 to |v|
        s[i, 0] ← 0
    for j ← 0 to |w|
        s[0, j] ← 0
    for i ← 1 to |v|
        for j ← 1 to |w|
            s[i, j] ← max{s[i-1, j], s[i,j-1], s[i-1, j-1] + 1 (if vi = wj)}
            if s[i,j] = s[i-1,j]
                Backtrack[i, j] ← "↓"
            if s[i, j] = s[i, j-1]
                Backtrack[i, j] ← "→"
            if s[i, j] = s[i-1, j-1] + 1
                Backtrack[i, j] ← "↘"

    return Backtrack
    ....

    :param v: string
    :param w: string
    :return: a backtrack matrix
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

    pprint(s)
    pprint(backtrack)
    return backtrack


def output_lcs(backtrack, v, i, j):
    """
    OUTPUTLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return
        if backtracki, j = "↓"
            OUTPUTLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "→"
            OUTPUTLCS(backtrack, v, i, j - 1)
        else
            OUTPUTLCS(backtrack, v, i - 1, j - 1)
            output vi
    :return:
    """

    result = ""

    while i >= 0:
        if backtrack[i][j] == 'd':
            i = i - 1
        elif backtrack[i][j] == 'a':
            j = j - 1
        else:
            result = v[i] + result
            i = i - 1
            j = j - 1

    return(result)

def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    v = "ABBCCDE"
    w = "AABCCDE"

    b = lcs_backtrack(v, w)

    r = output_lcs(b, v, len(v)-1, len(w)-1)

    print(r)


if __name__ == "__main__":
    sys.exit(main())