vertex = int(input())

adj_mat = []
for i in range(vertex):
    adj_mat.append([0]*(vertex))

for j in range(vertex):
    lst = list(map(int, input().split()))
    for k in range(1, lst[0]+1):
        adj_mat[j][lst[k]] = 1

for i in adj_mat:
    print(*i)