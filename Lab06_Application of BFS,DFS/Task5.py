#maximum distance between two nodes in a tree
from collections import deque
n=int(input())
adj_list=[[] for i in range(n+1)]
for i in range(1,n):
    u,v=map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(adj_list, start, N):
    dist=[-1]*(N+1)
    dist[start]=0
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if  dist[v]==-1:
                dist[v]=dist[u]+1
                queue.append(v)
    return dist

bfs_result1 = bfs(adj_list, 1, n)
max_dist1=0
max1=1
for i in range(1,n+1):
    if bfs_result1[i]>max_dist1:
        max_dist1=bfs_result1[i]
        max1=i

bfs_result2 = bfs(adj_list, max1, n)
max2=1
max_dist2=0
for i in range(1,n+1):
    if bfs_result2[i]>max_dist2:
        max2=i
        max_dist2=bfs_result2[i]
print(max_dist2)
print(max1, max2)



