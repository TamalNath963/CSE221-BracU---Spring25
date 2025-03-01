import sys
input = sys.stdin.readline

n = int(input())

trains = [[0]*3]*n

for i in range(n):
    s = input().split(" ")
    trains[i] = [s[0], s[4], s[6][:-1:]]

for i in range(n-1):
    flg = True
    for j in range(n-i-1):
        if trains[j][0] > trains[j + 1][0]:
            trains[j + 1], trains[j] = trains[j], trains[j+1]
            flg = False
        elif trains[j][0] == trains[j + 1][0] and trains[j][2] < trains[j+1][2]:
            trains[j + 1], trains[j] = trains[j], trains[j+1]

            flg = False
    if flg:
        break
for i in trains:
    print(f"{i[0]} will departure for {i[1]} at {i[2]}")


