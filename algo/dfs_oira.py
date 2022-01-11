from collections import deque

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n+1):
    g[i].sort(reverse=True)

ans = []
q = deque()
q.append(1)
checked = [False]*(n+1)
checked[1] = True
while q:
    v = q.pop()
    if v > 0:
        ans.append(v)
        for u in g[v]:
            if checked[u]:
                continue
            else:
                checked[u] = True
                q.append(-v)
                q.append(u)
    if v < 0:
        ans.append(-v)
print(*ans)