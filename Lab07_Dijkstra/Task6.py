#Shortest path revisited
n,m,s,d=map(int,input().split())
adj_list=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

import heapq
def dijkstra(adj_list, start, N):
    dist1= [float('inf')] * (N + 1)
    dist2= [float('inf')] * (N + 1)
    dist1[start] = 0
    heap=[(0,start)]
    while heap:
        curr_dist, u = heapq.heappop(heap)
        for v, w in adj_list[u]:
            new_dist=curr_dist+w
            if new_dist < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
            elif dist1[v] < new_dist < dist2[v]:
                dist2[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    return dist1,dist2

start_cost1,start_cost2=dijkstra(adj_list, s, n)
if start_cost2[d] == float('inf'):
    print(-1)
else:
    print(start_cost2[d])
            
        