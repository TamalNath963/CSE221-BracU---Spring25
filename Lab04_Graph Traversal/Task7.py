import math
n,q=map(int,input().split())
adj_lst=[[]for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and math.gcd(i,j)==1:
            adj_lst[i].append(j)

for i in range(q):
    x,k=map(int,input().split())
    neighbour=adj_lst[x]
    if len(neighbour)<k:
        print(-1)
    else:
        neighbour.sort()
        print(neighbour[k-1])












































# import math
 
# def precompute_coprimes(N):
#     coprime_neighbors = [[] for _ in range(N + 1)]
    
    
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if i != j and math.gcd(i, j) == 1:
#                 coprime_neighbors[i].append(j)
    
#     return coprime_neighbors
 
# def process_queries(coprime_neighbors, queries):
#     results = []
#     for X, K in queries:
#         neighbors = coprime_neighbors[X]
#         if len(neighbors) < K:
#             results.append(-1)
#         else:
            
#             neighbors.sort()
#             results.append(neighbors[K-1])
#     return results
 
 
# N, Q = map(int, input().split())  
# queries = [tuple(map(int, input().split())) for _ in range(Q)]
 
# coprime_neighbors = precompute_coprimes(N)
 
# results = process_queries(coprime_neighbors, queries)
# for result in results:
#     print(result)


