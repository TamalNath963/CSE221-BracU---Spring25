#the size of the subtree for each node in a tree using DFS.
n,r=map(int,input().split())
adj_list=[[] for i in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)


subtree_size = [0] * (n + 1)
parent = [0] * (n + 1)
stack = [r]
order = []

while stack:
    node = stack.pop()
    order.append(node)
    for neighbor in adj_list[node]:
        if neighbor != parent[node]:
            parent[neighbor] = node
            stack.append(neighbor)

order.reverse()

for i in order:
    node = i
    subtree_size[node] = 1
    for neighbor in adj_list[node]:
        if neighbor != parent[node]:
            subtree_size[node] += subtree_size[neighbor]


q = int(input())
for i in range(q):
    x = int(input())
    print(subtree_size[x])



#alternatife dfs with recursion

# n,r=map(int,input().split())
# adj_list=[[] for i in range(n+1)]
# for i in range(n-1):
#     u,v=map(int,input().split())
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# visited=[False]*(n+1)
# subtree_size=[0]*(n+1)
# def dfs(node):
#     visited[node]=True
#     size=1
#     for neighbor in adj_list[node]:
#         if  visited[neighbor]==False:
#             size+=dfs(neighbor)
            
#     subtree_size[node]=size
#     return size

# dfs(r)
# q=int(input())
# for i in range(q):
#     u=int(input())
#     print(subtree_size[u])