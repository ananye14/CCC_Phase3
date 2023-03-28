from collections import deque

n = int(input())  
adj = [[] for _ in range(n+1)]  
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
d = int(input())  
visited = set()  
queue = deque([(1, 1)]) 
count = 0  
while queue:
    node, level = queue.popleft()
    if node not in visited:
        visited.add(node)
        if level == d:
            count += 1
        for neighbor in adj[node]:
            if neighbor not in visited:
                queue.append((neighbor, level+1))
print(count)
