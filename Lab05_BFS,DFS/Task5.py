
# n,m=map(int, input().split())
# adj_list=[[] for i in range(n + 1)]
# for i in range(m):
#     u,v=map(int, input().split())
#     adj_list[u].append(v)
    
# visited=[-1]*(n+1)
# flag=[False]
# def dfs(adj_list, node, visited,flag):
#     visited[node]=0
#     for v in adj_list[node]:
#         if visited[v]==-1:
#             dfs(adj_list, v, visited,flag)
#             if flag[0]==True:
#                 return
#         elif visited[v]==0:
#             flag[0]=True
#             return
#     visited[node]=1
    
# for i in range(1,n+1):
#     if visited[i]==-1:
#         dfs(adj_list, i, visited,flag)
#         if flag[0]==True:
#             break

# # print("YES" if flag[0] else "NO")
# if flag[0]==True:
#     print("YES")
# else:
#     print("NO")



# #Alternative solution using stack


# import sys
# input = sys.stdin.readline
from collections import  deque

n, m = map(int, input().split())
adj_lst = [[] for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj_lst[u].append(v)

visited = [-1] * (n + 1)  

def dfs():
    for start in range(1, n + 1):
        if visited[start] == -1:
            stack = [start]
            #path = []
            while stack:
                node = stack[-1]
                if visited[node] == -1:
                    visited[node] = 0  
                    #path.append(node)
                    for neighbor in adj_lst[node]:
                        if visited[neighbor] == -1:
                            stack.append(neighbor)
                        elif visited[neighbor] == 0:
                            return True 
                else:
                    visited[node] = 1 
                    stack.pop()
    return False

if dfs():
    print("YES")
else:
    print("NO")