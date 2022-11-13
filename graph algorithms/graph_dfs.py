graph1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

already_visited = set()  # Set to keep track of visited nodes/cities


def dfs(visited, graph, node):
    if node not in visited:
        print(node)

        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(already_visited, graph1, 'A')
