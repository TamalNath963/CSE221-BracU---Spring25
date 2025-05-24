n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
indeg=[0]*(n+1)
outdeg=[0]*(n+1)
# for i in range(n+1):
#     indeg.append(0)
#     outdeg.append(0)
for i in range(m):
    outdeg[u[i]]+=1
    indeg[v[i]]+=1

for i in range(1,n+1):
    print(f"{indeg[i]-outdeg[i]}", end=" ")







































