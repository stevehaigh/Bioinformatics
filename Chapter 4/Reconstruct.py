"""
    File: Reconstruct
    Author: steve
    Created: 07/12/14
    
"""

from builtins import open, len, range, sorted
import sys

import OverlapGraph as og
import EulerianCycles as ec


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    # read file of kmers
    # create overlaps list
    # feed list in to eulerian path solver

    with open("kmers-2") as contents:
        kmers = [line.rstrip('\n').strip(' ') for line in contents]

    overlaps = og.find_overlaps(kmers[1:])

    with open("reconstruct-graph.txt", "w") as text_file:
        for key, value in overlaps.items():
            text_file.write(key + " -> " + ",".join(value) + "\n")

    with open("reconstruct-graph.txt") as contents:
        lines = [line.rstrip('\n') for line in contents]

    graph = ec.build_graph(lines)
    cycle = ec.find_cycle(graph)

    temp = []

    for node in cycle:
        temp.append(node.label)

    t2 = sorted(temp)
    t3 = sorted(kmers)

    print("\n".join(t2))
    print(".....")
    print("\n".join(t3))

    with open("reconstructed_path2.txt", "w") as text_file:
        for i in range(0, len(temp) - 1):
            text_file.write(temp[i][0])
        text_file.write(temp[i + 1])


if __name__ == "__main__":
    sys.exit(main())