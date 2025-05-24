n = int(input())
x,y = map(int,input().split())
ans = []
for dx in range(-1,2):
    for dy in range(-1,2):
        if dx==0 and dy==0:
            continue
        if 1<=dx+x<=n and  1<=dy+y<=n:
            ans.append((dx+x,dy+y))

print(len(ans))
for t in ans:
    print(f"{t[0]} {t[1]}")