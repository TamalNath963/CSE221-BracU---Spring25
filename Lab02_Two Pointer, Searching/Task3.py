n, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

j = 0
sum = 0
mxLength = 0

for i in range(n):
    sum += arr[i]
    if (sum > k):
        sum -= arr[j]
        j += 1
    if (sum <= k):
        mxLength=max(mxLength,i-j+1)
        
print(mxLength)
        
        

