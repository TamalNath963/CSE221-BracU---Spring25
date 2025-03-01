import sys
input = sys.stdin.readline
n =int(input())
arr = list(map(int, input().split()))
def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        flag=0
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=1
        if flag==0:
            break
    return arr

arr=bubbleSort(arr)
for i in arr:
    print(i,end=" ")
