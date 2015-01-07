"""
    File: TwoBreakDistance
    Author: steve
    Created: 06/01/15
    
"""
import sys


def calculate_number_of_cycles_in_graph(graph):
    """
    find the number of cycles in the graph by picking a random start point and traversing
    all connected nodes and removing that set from the graph, incrementing a counter for
    each set of connected nodes.
    :param graph:
    :return:
    """
    pass


def two_break_distance(p, q):
    """

    :param p: a set of lists of nodes, each list is a block
    :param q: ditto
    :return: the 2-break distance between p and q
    """

    # first build a single graph by connecting all elements in each block
    # e.g. (a,b,c) => a<->b<->c<->a
    # each edge is undirected so add a->b and b->a etc to the graph
    pq_graph = {}

    # CYCLES(p,q)
    number_of_cycles = calculate_number_of_cycles_in_graph(pq_graph)

    # BLOCKS(p,q)
    # simply the sum of all the nodes in every block in p (or q)
    number_of_blocks = 0
    for block in p:
        number_of_blocks += len(block)

    return number_of_blocks - number_of_cycles


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv


if __name__ == "__main__":
    sys.exit(main())