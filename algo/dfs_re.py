import sys
sys.setrecursionlimit(10000)

n, m = map(int,input().split())
cnt = 0
g=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

def dfs(v):
    if checked[v] == 1:
        return
    checked[v] = 1
    for j in g[v]:
        dfs(j)

for i in range(n):
    checked=[0]*(n)
    dfs(i)
    cnt += sum(checked)
