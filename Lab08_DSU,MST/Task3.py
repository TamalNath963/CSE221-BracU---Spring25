def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x == root_y:
        return
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def mst_kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    mst = []
    total_weight = 0
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
            total_weight += w
    
    return mst, total_weight

def main():
    n, m = map(int, input().split())
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    mst, mst_weight = mst_kruskal(n, edges)
    
    if len(mst) < n - 1:
        print(-1)
        return
    
    mst_edges = set()
    for u, v, _ in mst:
        mst_edges.add((min(u, v), max(u, v)))
    
    min_second_mst = float('inf')
    
    for i, e in enumerate(mst):
        u, v, w = e
        
        mst_without_edge = mst[:i] + mst[i+1:]
        
        min_replacement = float('inf')
        
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        for x, y, _ in mst_without_edge:
            union(parent, rank, x, y)
        
        for x, y, wt in edges:
            if (min(x, y), max(x, y)) == (min(u, v), max(u, v)):
                continue
                
            if (min(x, y), max(x, y)) in mst_edges:
                continue
                
            if find(parent, x) != find(parent, y):
                new_weight = mst_weight - w + wt
                if new_weight > mst_weight and new_weight < min_replacement:
                    min_replacement = new_weight
        
        if min_replacement < float('inf'):
            min_second_mst = min(min_second_mst, min_replacement)
    
    print(min_second_mst if min_second_mst < float('inf') else -1)

if __name__ == "__main__":
    main()
