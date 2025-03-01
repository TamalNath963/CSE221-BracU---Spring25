import sys
input = sys.stdin.readline
n =int(input())
id = list(map(int, input().split()))
mark=list(map(int, input().split()))
temp=0
for i in range(len(id)-1):
    max=i
    for j in range(i+1,len(id)):
        if mark[j]>mark[max]:
            max=j
        elif mark[j]==mark[max] and id[j]<id[max]:
            max=j
    if max!=i:
        temp+=1
        mark[i],mark[max]=mark[max],mark[i]
        id[i],id[max]=id[max],id[i]

print(f"Minimum swaps: {temp}")
for i in range(len(id)):
    print(f"ID: {id[i]} Mark: {mark[i]}")
                                            