n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
deg=[0]*(n+1)
for i in range(m):
    deg[u[i]]+=1
    deg[v[i]]+=1

count=0
for i in range(1,n+1):
    if deg[i]%2!=0:
        count+=1
    
if count==0 or count==2:
    print("YES")
else:
    print("NO")