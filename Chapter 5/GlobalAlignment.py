"""
    File: LCS
    Author: steve
    Created: 30/12/14
    
"""
from pprint import pprint
import sys



def make_blosum62():
    rows = """A 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7""".split('\n')

    blosum_lookup = {}
    bases = "A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y".split()
    for row in rows:        
        scores = row.split()
        row_dict = {}
        for i in range(0, len(bases)):
            row_dict[bases[i]] = int(scores[i+1])

        blosum_lookup[scores[0]] = row_dict
        
    return blosum_lookup


def lcs_backtrack(v, w, sigma):
    """
    Finds the LCS backtrack matrix for two strings, v and w
    """
    ##print(v,w)
    indel_penalty = sigma

    s = [x[:] for x in [[0]*(len(w)+1)]*(len(v)+1)]
    backtrack = [x[:] for x in [['-']*(len(w)+1)]*(len(v)+1)]
    blosum_lookup_table = make_blosum62()

    ## init the top and side columns with indel penalty
    for i in range(0, len(v)):
        s[i][0] = -i * sigma

    for j in range(0, len(w)):
        s[0][j] = -j * sigma



    for i in range(0, len(v)):
        for j in range(0, len(w)):                
            s[i+1][j+1] = max(s[i][j+1] - indel_penalty, s[i+1][j] - indel_penalty, s[i][j] + blosum_lookup_table[v[i]][w[j]])
            if s[i+1][j+1] == s[i][j] + blosum_lookup_table[v[i]][w[j]]:
                backtrack[i+1][j+1] = '#'
            elif s[i+1][j+1] == s[i][j+1] - indel_penalty:
                backtrack[i+1][j+1] = 'd'
            elif s[i+1][j+1] == s[i+1][j] - indel_penalty:
                backtrack[i+1][j+1] = 'a'
            else:
                backtrack[i+1][j+1] = '!'
        
    ##pprint(backtrack)
    ##pprint(s)
    return backtrack, s[len(v)][len(w)]


def output_lcs(backtrack, v, w, i, j):
    result1 = ""
    result2 = ""
    result3 = ""
    lcs = ""

    while i > 0 and j > 0:         

        if backtrack[i][j] == 'd':    
            result1 = v[i-1] + result1      
            result2 = "-" + result2
            result3 = "-" + result3             
            i = i - 1   

        elif backtrack[i][j] == 'a':     
            result1 = "-" + result1      
            result2 = w[j-1] + result2
            result3 = "-" + result3
            j = j - 1
            
        else:            
            result1 = v[i-1] + result1      
            result2 = w[j-1] + result2
            result3 = v[i-1] + result3
            lcs = v[i-1] + lcs
            i = i - 1
            j = j - 1

    # tidy up any leading "-" needed
    while i > 0:
        result1 = v[i-1] + result1
        result2 = "-" + result2
        result3 = "-" + result3
        i = i - 1

    while j > 0:      
        result1 = "-" + result1  
        result2 = w[j-1] + result2
        result3 = "-" + result3
        j = j -1

    return (result1, result2, result3, lcs)

def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    w = "ACC"
    v = "ADC"
    sigma = 5

    b, score = lcs_backtrack(v, w, sigma)

    r1,r2,r3,lcs = output_lcs(b, v, w, len(v), len(w))

    print(score)
    print(r2)
    print(r1)
    #print(r3)
    #print("................")
    #print(lcs)


if __name__ == "__main__":
    main()
    #sys.exit(main())