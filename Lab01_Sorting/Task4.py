# T = int(input())
# for i in range(T):
#     N = int(input())
#     sum= N*(N+1)//2
#     print(sum)


import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
count=0
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    if min!=i:
        arr[i],arr[min]=arr[min],arr[i]
        count+=1
print(count)

# import sys
# input=sys.stdin.readline
# n,k=map(int, input().split())
# arr=list(map(int, input().split()))
# count=0
# for i in range(n-1):
#     max=i
#     for j in range(i+1,n):
#         if arr[j]>arr[max]:
#             max=j
#     if max!=i:
#         arr[i],arr[max]=arr[max],arr[i]
#         count+=1
# if count<=k:
#     print("Possible")
# else:
#     print("Impossible")