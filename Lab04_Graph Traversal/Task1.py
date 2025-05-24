n,m=map(int,input().split())
adj_mat=[]
for i in range(n):
        row = [0] * n
        adj_mat.append(row)
for i in range(m):
    u,v,w=map(int,input().split())
    adj_mat[u-1][v-1]=w
for i in adj_mat:
    print(*i)