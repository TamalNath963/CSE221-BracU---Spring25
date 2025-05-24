#where to meet
n,m,s,t=map(int,input().split())
adj_list=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))

import heapq
def dijkstra(adj_list, start, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

dist_s = dijkstra(adj_list, s, n)
dist_t = dijkstra(adj_list, t, n)

min_time=float('inf')
node=-1
for i in range(1,n+1):
    if dist_s[i]!=float('inf') and dist_t[i]!=float('inf'):
        time=max(dist_s[i],dist_t[i])
        if time<min_time:
            min_time=time
            node=i
        if time==min_time:
            if i<node:
                node=i
if min_time==float('inf'):
    print(-1)
else:
    print(min_time, node)
    