#dijkstra algorithm
#find the shortest path from s to d in a directed graph with n vertices and m edges

n,m,s,d=map(int,input().split())
adj_list=[[] for i in range(n+1)]
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(m):
    adj_list[u[i]].append((v[i],w[i]))

import heapq
def dijkstra(adj_list, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    parent= [None] * (n + 1)
    heap= [(0, start)]  # (distance, node)

    while heap:
        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        for v, weight in adj_list[u]:
            if dist[u] + weight < dist[v]:         #edge relaxation
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, parent

dist,parent = dijkstra(adj_list, s, n)
if dist[d] == float('inf'):
    print(-1)
else:
    print(dist[d])
    path = []
    current = d
    while current !=None:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(*path) 
    



            