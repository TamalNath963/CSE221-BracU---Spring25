#finding the maximum number of vertices in a bipartite graph.
from collections import deque
n,m=map(int,input().split())
adj_list=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

color=[-1]*(n+1)

def bipartite(adj_list,color):
    total=0
    for i in range(1,n+1): 
       if color[i]==-1:
          color[i]=0
          queue=deque()
          queue.append(i)
          count0,count1=1,0
          while queue:
             u=queue.popleft()
             for v in adj_list[u]:
                if color[v]==-1:
                   color[v]=1-color[u]
                   if color[v]==0:
                     count0+=1
                   else:
                     count1+=1
                   queue.append(v)
                elif color[v]==color[u]:
                   return -1
          total+=max(count0,count1)
    return total
    

x=bipartite(adj_list,color)
if x==-1:
    print("NO")
else:
    print(x)


    
    
    
