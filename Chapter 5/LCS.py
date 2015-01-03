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
    """
    print(v,w)

    s = [x[:] for x in [[0]*(len(w)+1)]*(len(v)+1)]
    backtrack = [x[:] for x in [['-']*(len(w)+1)]*(len(v)+1)]

    for i in range(0, len(v)):
        for j in range(0, len(w)):
            if v[i] == w[j]:
                s[i+1][j+1] = s[i][j] + 1
                backtrack[i+1][j+1] = '#'
            else:                
                s[i+1][j+1] = max(s[i][j+1], s[i+1][j])

                if s[i+1][j+1] == s[i][j+1]:
                    backtrack[i+1][j+1] = 'd'
                elif s[i+1][j+1] == s[i+1][j]:
                    backtrack[i+1][j+1] = 'a'
                else:
                    backtrack[i+1][j+1] = '!'
        
    ##pprint(backtrack)
    ##pprint(s)
    return backtrack


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

    v = "PLEASANTLY"
    w = "MEANLY"

    b = lcs_backtrack(v, w)

    r1,r2,r3,lcs = output_lcs(b, v, w, len(v), len(w))

    print(r1)
    print(r2)
    print(r3)
    print("................")
    print(lcs)
    print("................")

    edit_distance = max(len(v), len(w)) - len(lcs)
    print("Edit distance = " + str(edit_distance))


if __name__ == "__main__":
    main()
    #sys.exit(main())