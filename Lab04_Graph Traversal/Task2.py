n,e=map(int,input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
w=list(map(int, input().split()))

adj_lst=[[] for i in range(n+1)]

for i in range(e):
    adj_lst[u[i]].append((v[i],w[i]))

for i in range(1,n+1):
    row=f"{i}:"
    for v,w in adj_lst[i]:
        row+=f" ({v},{w})"
    
    print(row)

