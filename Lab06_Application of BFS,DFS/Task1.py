#Topological sort using Kahn's algorithm(BFS)
from collections import deque
n,m=map(int,input().split())
adj_list=[[]for i in range(n+1)]
indegree=[0]*(n+1)
for i in range(m):
    u,v=map(int,input().split())
    adj_list[u].append(v)
    indegree[v]+=1

queue=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        queue.append(i)
list=[]
while queue:
    u=queue.popleft()
    list.append(u)
    for v in adj_list[u]:
        indegree[v]-=1
        if indegree[v]==0:
            queue.append(v)

if len(list)==n:
    print(*list)
else:
    print("-1")   