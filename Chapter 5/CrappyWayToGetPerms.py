"""
    File: CrappyWayToGetPerms
    Author: steve
    Created: 22/12/14
    
"""
import sys
import math


def main(argv=None):


    count = 0

    for i in range(0, 11):
        for j in range(0, 8):
            if (i*2) + (j*3) == 20:
                print(i, j)
                n = i + j
                r = i
                combinations = math.factorial(n)/(math.factorial(r) * math.factorial(n - r))

                count += combinations
                print(combinations)
                print("........")

    print("........")
    print(count)



if __name__ == "__main__":
    sys.exit(main())