def dfs(node):
    visited[node] = True
    size = 1
    for neighbor in adj[node]:
        if not visited[neighbor]:
            size += dfs(neighbor)
    return size

n, m = map(int, input().split())  # number of nodes and edges
adj = [[] for _ in range(n+1)]  # adjacency list to represent the forest
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n+1)  # boolean array to keep track of visited nodes
trees = 0  # number of trees in the forest
sizes = []  # list of sizes of trees in the forest

for node in range(1, n+1):
    if not visited[node]:
        size = dfs(node)
        trees += 1
        sizes.append(size)

if trees == 0:
    print("0 0 0")
else:
    print(max(sizes), min(sizes), trees)
