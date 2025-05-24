# Problem: Alien Dictionary
import heapq
n = int(input())
word=[]
for i in range(n):
    word.append(input())

graph = [[] for _ in range(26)]
in_degree = [0] * 26
present = [False] * 26

for w in word:
    for char in w:
        present[ord(char) - ord('a')] = True

for i in range(n - 1):
    w1 = word[i]
    w2 = word[i + 1]
    len1 = len(w1)
    len2 = len(w2)
    length = min(len1, len2)
    diff = False
    for j in range(length):
        if w1[j] != w2[j]:
            u = ord(w1[j]) - ord('a')
            v = ord(w2[j]) - ord('a')
            if v not in graph[u]:
                graph[u].append(v)
                in_degree[v] += 1
            diff = True
            break
    if  not diff and len1 > len2:
        print(-1)
        exit()
        
heap = []
for i in range(26):
    if present[i]==True and in_degree[i] == 0:
        heapq.heappush(heap,i)

result = ""
count = 0

while heap:
    u = heapq.heappop(heap)
    result += chr(ord('a') + u)
    count += 1
    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            heapq.heappush(heap, v)

present_count = sum(present)
if count == present_count:
    print(result)
else:
    print(-1)