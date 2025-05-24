import sys
input=sys.stdin.readline
n=int(input())
arr1=list(map(int,input().split()))
k=int(input())
arr2=list(map(int,input().split()))
arr=[]
i=0
j=0
while i<n and j<k:
    if arr1[i]<arr2[j]:
        arr.append(arr1[i])
        i+=1
    else: 
        arr.append(arr2[j])
        j+=1
if i<n or j<k:
    if i<n:
        for l in range(i,n):
            arr.append(arr1[l])
    else:
        for l in range(j,k):
            arr.append(arr2[l])

for i in arr:
    print(i,end=" ")
    

