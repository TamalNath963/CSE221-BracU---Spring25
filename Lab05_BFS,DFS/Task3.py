from collections import deque
n,m,s,d=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))

adj_list = [[] for i in range(n + 1)]
for i in range(m):
    adj_list[u[i]].append(v[i])
    adj_list[v[i]].append(u[i])

for i in range(1, n + 1):
    adj_list[i].sort()

dist=[-1]*(n+1)
parent=['null']*(n+1)
dist[s]=0
queue=deque()
queue.append(s)
while queue:
    u=queue.popleft()
    for v in adj_list[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            parent[v]=u
            queue.append(v)

if dist[d]==-1:
    print(-1)
else:
    print(dist[d])
    path=[]
    curr=d
    while curr!='null':
        path.append(curr)
        curr=parent[curr]
    path.reverse()
    print(*path)

