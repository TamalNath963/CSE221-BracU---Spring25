
N,K = map(int, input().split())
parent = [i for i in range(N + 1)]
size = [1] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]
    return size[rootX if rootX == find(x) else rootY]


output = []
for _ in range(K):
    a,b= map(int, input().split())
    
    output.append(str(union(a, b)))

for i in output:
    print(i)


