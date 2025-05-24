n, q = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))


def LowerBound(arr, target):
    lo = 0
    hi = len(arr)-1
    mid = -1
    while lo < hi:
        mid = (hi+lo)//2
        if (target <= arr[mid]):
            hi = mid
        else:
            lo = mid + 1
    if (arr[lo] >= target):
        return lo
    if (arr[hi] >= target):
        return hi
    return len(arr)


def upperBound(arr, target):
    lo = 0
    hi = len(arr)-1
    while lo < hi:
        mid = (hi+lo)//2
        if (target < arr[mid]):
            hi = mid
        else:
            lo = mid + 1

    if (arr[lo] > target):
        return lo
    if (arr[hi] > target):
        return hi
    return len(arr)


for i in range(q):
    s, e = map(int, input().split(" "))
    print(upperBound(arr, e)-LowerBound(arr, s))
