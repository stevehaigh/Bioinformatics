"""
    File: ManhattenTourist
    Author: steve
    Created: 21/12/14
    
"""
import sys
import Matrix


def get_longest_path(m, n, down, right):
    """
    MANHATTANTOURIST(n, m, Down, Right)
        s0, 0 ‚?ê 0
        for i ‚?ê 1 to n
            si, 0 ‚?ê si-1, 0 + downi, 0
        for j ‚?ê 1 to m
            s0, j ‚?ê s0, j‚??1 + right0, j
        for i ‚?ê 1 to n
            for j ‚?ê 1 to m
                si, j ‚?ê max{si - 1, j + downi, j, si, j - 1 + righti, j}
        return sn, m
    :param m:
    :param n:
    :param down:
    :param across:
    :return:
    """

    s = [x[:] for x in [[0]*(m+1)]*(n+1)]

    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]

    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])

    return s[n][m]



def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    n = 11
    m = 10

    down_txt = """1 3 4 4 3 1 4 3 1 4 3
4 2 4 3 3 2 4 4 2 2 2
2 1 4 2 0 2 4 0 1 1 2
2 1 0 2 3 1 4 0 0 4 3
0 4 2 3 4 3 3 4 1 3 3
4 0 3 4 3 0 4 4 3 2 3
4 1 4 2 1 0 4 2 0 2 1
4 0 0 3 1 3 4 3 0 2 1
1 3 2 1 3 3 3 2 0 3 2
0 4 0 2 3 1 1 2 4 4 4
0 4 4 4 3 4 1 2 3 0 4"""

    right_txt = """1 4 4 1 0 2 0 3 0 3
0 2 4 1 2 0 1 2 3 2
4 0 0 1 4 0 1 0 3 0
0 4 2 3 4 1 2 2 0 4
4 4 3 4 0 4 1 2 4 2
0 2 2 1 3 1 0 4 2 3
3 2 3 4 2 2 3 2 2 3
1 0 4 2 1 3 4 4 0 0
3 4 1 3 1 2 3 3 3 2
4 0 4 3 0 4 2 4 0 0
4 4 2 4 1 4 2 2 2 4
1 2 1 0 0 3 1 4 1 1"""

    down = Matrix.create_matrix(down_txt)
    right = Matrix.create_matrix(right_txt)

    print(get_longest_path(m,n,down,right))


if __name__ == "__main__":
    sys.exit(main())