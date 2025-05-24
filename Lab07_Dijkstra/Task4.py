n,m,s,d=map(int,input().split())
weights=list(map(int,input().split()))
adj_list=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    adj_list[u].append(v)

import heapq
def dijkstra(adj_list, start, N):
    cost= [float('inf')] * (N + 1)
    cost[start] = weights[start-1]
    heap=[(cost[start],start)]
    while heap:
        curr_cost, u = heapq.heappop(heap)
        if curr_cost > cost[u]:
            continue
        for v in adj_list[u]:
            new_cost=curr_cost+weights[v-1]
            if new_cost < cost[v]:
                cost[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    return cost

start_cost=dijkstra(adj_list, s, n)
if start_cost[d] == float('inf'):
    print(-1)
else:
    print(start_cost[d])

    