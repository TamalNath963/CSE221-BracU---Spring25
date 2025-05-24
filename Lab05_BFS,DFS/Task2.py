import sys
sys.setrecursionlimit(2*100000+5)
n,m=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
adj_list = [[] for i in range(n + 1)]
for i in range(m):
    adj_list[u[i]].append(v[i])
    adj_list[v[i]].append(u[i])

for i in range(1, n + 1):
    adj_list[i].sort()

visited = [False] * (n + 1)
result = []
def dfs(adj_list, node, visited, result):
    visited[node] = True
    result.append(node)
    for v in adj_list[node]:
        if visited[v] == False:
            dfs(adj_list, v, visited, result)
    return result

x=dfs(adj_list, 1, visited, result)
print(*x)