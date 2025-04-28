def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()  # For DFS
    visited2 = set()  # For BFS
    queue = []        # For BFS
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n+1):
        graph[i] = []

    e = int(input("Enter number of edges: "))
    for _ in range(e):
        u, v = map(int, input("Enter an edge (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph: add both ways

    print("\nThe following is DFS traversal:")
    dfs(visited1, graph, 1)

    print("\n\nThe following is BFS traversal:")
    bfs(visited2, graph, 1, queue)

if __name__ == "__main__":
    main()
