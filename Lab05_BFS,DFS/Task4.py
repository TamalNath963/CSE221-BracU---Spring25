from collections import deque
n,m,s,d,k=map(int, input().split())
adj_list = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    
def bfs(adj_list,s,n):
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
    return dist,parent

def path_print(parent,d):
    path=[]
    curr=d
    while curr!='null':
        path.append(curr)
        curr=parent[curr]
    path.reverse()
    return path

dist_s,parent_s=bfs(adj_list,s,n)
dist_k,parent_k=bfs(adj_list,k,n)

if dist_s[k]==-1 or dist_k[d]==-1:
    print(-1)
else:
    print(dist_s[k]+dist_k[d])
    path=path_print(parent_s,k)+path_print(parent_k,d)[1:]
    print(*path)
    # path1=path_print(parent_s,k)
    # path2=path_print(parent_k,d)
    # ans=[]
    # for i in range(1,len(path2)):
    #     ans.append(path2[i])
    # path=path1+ans
    # print(*path)
