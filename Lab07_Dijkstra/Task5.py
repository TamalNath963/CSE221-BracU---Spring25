import heapq
n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
adj_list = [[] for i in range(n + 1)]
for i in range(m):
    adj_list[u[i]].append((v[i], w[i]))
    
# dist[u][0] = min cost to u with last edge even
# dist[u][1] = min cost to u with last edge odd
dist = [[float('inf'), float('inf')] for i in range(n + 1)]
heap = []

# Starting from node 1, we consider all edges out of node 1
for v, w in adj_list[1]:
    parity = w % 2
    if w < dist[v][parity]:
        dist[v][parity] = w
        heapq.heappush(heap, (w, v, parity))

while heap:
    cost_u, u, parity_u = heapq.heappop(heap)
    if cost_u > dist[u][parity_u]:
        continue
    for v, w in adj_list[u]:
        parity_v = w % 2
        if parity_v == parity_u:
            continue  # cannot take same parity twice in a row
        new_cost = cost_u + w
        if new_cost < dist[v][parity_v]:
            dist[v][parity_v] = new_cost
            heapq.heappush(heap, (new_cost, v, parity_v))

ans = min(dist[n][0], dist[n][1])
if ans==float('inf'):
    print(-1)
else:
    print(ans)
