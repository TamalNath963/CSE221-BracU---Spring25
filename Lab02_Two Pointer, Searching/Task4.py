T=int(input())
for i in range(T):
    n=0
    st=input()
    for i in range(len(st)):
        if st[i]=="1":
            n=i+1
            break
    if n==0:
        print("-1")
    else:
        print(n)


    
# def LowerBound(arr, target):
#     lo = 0
#     hi = len(arr)-1
#     while lo < hi:
#         mid = (hi+lo)//2
#         if (target <= int(arr[mid])):
#             hi = mid
#         else:
#             lo = mid + 1
#     if (int(arr[lo]) == target):
#         return lo+1
#     if (int(arr[hi]) == target):
#         return hi+1
#     return -1
# T=int(input())
# for i in range(T):
#     arr =  input()
#     print(LowerBound(arr, 1))
