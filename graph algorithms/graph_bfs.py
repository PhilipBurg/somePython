# 1. creating some graph structure
# task, find path from Frankfurt to München

graph = {
    'Frankfurt': ["Mannheim", "Würzburg", "Kassel"],
    'Mannheim': ["Karlsruhe"],
    'Würzburg': ["Nürnberg", "Erfurt"],
    'Kassel': ["München"],
    'Karlsruhe': ["Augsburg"],
    'Nürnberg': ["Stuttgart"],
}


def breadth_first_search(graph, start='Frankfurt', end='München'):
    visited = {start: None}
    queue = [start]
    path = []

    while queue:
        node = queue.pop(0)

        if node == end:
            while node is not None:
                path.append(node)
                node = visited[node]
            print("Here is the path from {} to {}:".format(start, end))
            return path[::-1]
        try:
            neighbors = graph[node]
        # for example if you reach the number 4 in graph, 4 is no key in this dict
        except KeyError:
            continue

        for n in neighbors:
            visited[n] = node
            queue.append(n)

        print('Node: ', node)
        print('Neighbors: ', neighbors)
        print('Already visited: ', visited)
        print('Queue; ', queue)
        print('')


print(breadth_first_search(graph))
