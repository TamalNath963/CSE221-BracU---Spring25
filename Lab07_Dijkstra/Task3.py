#Minimize the danger
n,m=map(int,input().split())
adj_list=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    adj_list[u].append((v,w))
    adj_list[v].append((u,w)) 

import heapq
def dijkstra(adj_list, start, N):
    danger = [float('inf')] * (N + 1)
    danger[start] = 0
    heap = [(0, start)]      # (Current danger, node)

    while heap:
        curr_danger, u = heapq.heappop(heap)
        if curr_danger > danger[u]:
            continue
        for v, w in adj_list[u]:
            new_danger=max(curr_danger, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(heap, (new_danger, v))

    return danger

ans=[]
danger=dijkstra(adj_list, 1, n)
for i in range(1,n+1):
    if danger[i]==float('inf'):
        ans.append(-1)
    else:
        ans.append(danger[i])
print(*ans)
