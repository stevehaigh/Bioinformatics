"""
    File: DPChange
    Author: steve
    Created: 16/12/14
    
"""
import sys


def dp_change(money, coins):
    """
     DPCHANGE(money, Coins)
     MinNumCoins(0) ← 0
     for m ← 1 to money
        MinNumCoins(m) ← ∞
            for i ← 1 to |Coins|
                if m ≥ coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) ← MinNumCoins(m - coini) + 1
    output MinNumCoins(money)
    :return:
    """

    min_num_of_coins = [0]

    if money <= 0:
        return 0

    for m in range(1, money+1):
        min_num_of_coins.append(sys.maxsize)
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if min_num_of_coins[m - coins[i]] + 1 < min_num_of_coins[m]:
                    min_num_of_coins[m] = min_num_of_coins[m - coins[i]] + 1

    return min_num_of_coins[money]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    coins = [2,3]
    money = 20


    print(str(dp_change(money, coins)))


if __name__ == "__main__":
    sys.exit(main())