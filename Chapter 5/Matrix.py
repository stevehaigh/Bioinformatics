"""
    File: Matrix
    Author: steve
    Created: 21/12/14
    
"""


def create_matrix(nums):
    """

    :param nums: a string of numbers, separated by spaces and line breaks
    :return: a list of lists, which can be indexed by matrix[x][y]
    """

    lines = nums.split('\n')
    matrix = []

    for line in lines:
        temp = line.strip(' ').split(' ')
        row = list(map(int, temp))
        matrix.append(row)

    return matrix