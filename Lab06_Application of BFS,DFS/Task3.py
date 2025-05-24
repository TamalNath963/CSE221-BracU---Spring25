from collections import deque

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
direction = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

dist=[]
for i in range(n + 1):
    dist.append([-1] * (n + 1))
        
queue = deque([(x1, y1, 0)])
dist[x1][y1] = 0

while queue:
    crntX, crntY, crntDist = queue.popleft()
    if crntX == x2 and crntY == y2:
        print(crntDist)
        exit()
    for dx, dy in direction:
        nxtX, nxtY = crntX + dx, crntY + dy
        if 1 <= nxtX <= n and 1 <= nxtY <= n and dist[nxtX][nxtY] == -1:
            dist[nxtX][nxtY] = crntDist + 1
            queue.append((nxtX, nxtY, crntDist + 1))
        
print(-1) 