n,m=map(int, input().split())
adj_list = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
    
for i in range(1, n + 1):
    adj_list[i].sort()

def bfs(adj_list, start, N):
    visited = [False] * (N + 1)
    queue = [start]
    visited[start] = True
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in adj_list[u]:
            if  visited[v]==False:
                visited[v] = True
                queue.append(v)

    return result
bfs_result = bfs(adj_list, 1, n)
print(*bfs_result)