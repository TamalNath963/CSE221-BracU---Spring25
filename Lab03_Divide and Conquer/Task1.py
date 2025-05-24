def merge(arr, start, end):
    i= start
    mid = (start + end) // 2
    j=mid+1
    inv = 0
    tmp=[]

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            inv += (mid - i + 1)
            tmp.append(arr[j])
            j+=1
        

    while i <= mid:
        tmp.append(arr[i])
        i+=1
    while j <= end:
        tmp.append(arr[j])
        j+=1
    k = 0
    for i in range(start,end+1):
        arr[i] = tmp[k]
        k+=1
    return inv

def invert(arr, start, end):
    if (start >= end):
        return 0
    mid =(start + end) // 2
    return invert(arr, start, mid) +invert(arr, mid + 1, end) + merge(arr, start, end)


n = int(input())
arr = list(map(int, input().split()))
print(invert(arr,0,n-1))
for i in arr:
    print(f"{i} ",end="")