
import sys
class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


def calculate_max_path_to_node(cache, edges, start_node, node_label):
    """
    Cache will store max weight to each node and a string representation of the path to that node.
    """

    
    if not node_label in cache:
        # calc inbound path
        if node_label == start_node:
            # we're done
            cache[node_label] = (0, node_label)
        else:
            # calc maximal inbound path for this node. 
            # Init the list to large negative number to penalize nodes with no inbound edges. This is a nasty hack!
            all_inbound_weights = [((sys.maxsize * -1) + 1, '-')]           

            for edge in [e for e in edges if e.to_node == node_label]:
                max_inbound = calculate_max_path_to_node(cache, edges, start_node, edge.from_node)
                weight = edge.weight + max_inbound[0]
                all_inbound_weights.append((weight, max_inbound[1] + "->" + node_label))

            max = sys.maxsize * -1
            inbound = ()
            for temp in all_inbound_weights:
                if temp[0] > max:
                    max = temp[0]
                    inbound = temp

                cache[node_label] = inbound    
        
    return cache[node_label]


def main(argv=None):
    """
    :param argv: the command line args
    :return: nothing
    """
    if argv is None:
        argv = sys.argv

    start_node = "11"
    end_node = "27"

    all_edges = []

    all_edges_text = """10->19:24
4->8:7
15->26:37
15->21:3
15->24:8
18->26:5
18->27:17
10->14:21
18->22:13
4->6:5
11->14:19
11->15:25
8->22:32
4->11:8
1->13:37
1->10:27
4->10:34
9->15:30
20->25:11
1->16:4
1->18:5
1->19:5
10->25:10
10->26:38
10->20:8
10->21:8
15->16:4
15->25:39
3->20:8
7->18:10
9->19:9
7->13:32
7->16:30
8->17:4
4->18:2
8->11:24
8->10:20
16->17:36
6->9:9
6->8:11
4->27:29
7->24:36
22->24:39
26->27:34
4->17:22
6->26:26
7->20:30
7->23:4
7->25:10
1->3:4
13->15:25
13->19:19
1->9:30
5->12:17
6->22:5
5->10:26
0->23:9
0->20:28
13->27:10
12->17:12
3->5:7
12->13:4
0->4:35
0->6:38
24->25:36
6->10:14
0->3:27
11->20:0
11->23:5
11->26:22
19->21:35
17->24:13
8->9:17
17->22:2
19->24:27
2->18:37
3->10:24
3->11:10
3->13:1
2->13:19
2->17:24
5->13:38
18->23:0
2->22:24
2->23:28
5->22:32
0->15:38
0->13:36
0->11:17
21->27:5
12->26:5
12->27:2
25->27:34
12->20:18"""

    all_edges_lines = all_edges_text.strip(' ').split('\n')

    for line in all_edges_lines:
        from_to, weight = line.split(':')
        from_node, to_node = from_to.split('->')
        all_edges.append( Edge(from_node.strip(' '), to_node, int(weight)) )

    weight = calculate_max_path_to_node({}, all_edges, start_node, end_node)

    print(weight[0])
    print(weight[1])


if __name__ == "__main__":
    main()
    #sys.exit(main())