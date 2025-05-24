
N,M=map(int, input().split())
edges = []
for _ in range(M):
    u,v,w=map(int,input().split())
    edges.append((w, u, v))
    
edges.sort()
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
    return True

total_cost = 0
for w, u, v in edges:
    if union(u, v):
        total_cost += w

print(total_cost)



