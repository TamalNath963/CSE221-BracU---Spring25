# import numpy as np
# i = input()
# n, k = i.split(" ")
# n = int(n)
# k = int(k)
# arr = np.array([0] * n)
# inputData = input().split(" ")
# for i in range(len(arr)):
#     arr[i] = int(inputData[i])
# start,end=0,len(arr)-1
# while start<end:
#     arr[start],arr[end]=arr[end],arr[start]
#     start+=1
#     end-=1
# for i in range(n - k, n):
#     print(f"{arr[i]} ", end="")
##############################################################################
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
i =0
j=n-1
while i<j:
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
for i in range(n-k,n):
    print(f"{arr[i]} ",end="")
