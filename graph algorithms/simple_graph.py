class Graph:
    def __init__(self, numb_of_nodes, edges):
        self.numb_of_nodes = numb_of_nodes
        # creating a list of lists
        self.adj_list = [[] for _ in range(numb_of_nodes)]
        for n1, n2 in edges:
            # now insert into the right lists
            self.adj_list[n1].append(n2)
            self.adj_list[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{} : {}".format(n, neighbours) for n, neighbours in enumerate(self.adj_list)])

    def __str__(self):
        return self.__repr__()


graph_1 = Graph(5, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])

print(graph_1)