n=int(input())
arr = list(map(int, input().split(" ")))
def bst(arr,s,e):
    if s==e:
        print(arr[s],end=" ")
        return
    if s>e:
        return
    else:
        mid=(s+e)//2
        print(arr[mid],end=" ")
        bst(arr,s,mid-1)
        bst(arr,mid+1,e)
bst(arr,0,n-1)