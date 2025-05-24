import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=list(map(int,input().split()))
def sumTrouble(arr,k):
      i=0
      j=len(arr)-1
      while i<j:
         if (arr[i]+arr[j])==k:
             return(f"{i+1} {j+1}")
         elif (arr[i]+arr[j])<k:
             i+=1
         elif(arr[i]+arr[j])>k:
             j-=1
      return-1
print(sumTrouble(arr,k))





























# flag=True
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if (arr[i]+arr[j])==k:
#             print(f"{i+1} {j+1}")
#             flag=False
#     if flag==False:
#         break
# if flag:
#     print("-1")