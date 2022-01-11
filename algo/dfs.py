import collections

n,q=map(int,input().split())
cnt=[0]*(n+1)
g=[[] for _ in range(n+1)]
for _ in range(n-1): #木グラフの隣接リストを作成
 a,b=map(int,input().split())
 g[a].append(b)
 g[b].append(a)
for _ in range(q): #各頂点についてcount[v]を計算
 v,val=map(int,input().split())
 cnt[v]+=val
q=collections.deque()
q.append(1) #DFSのスタックによる実装、まずスタックに始点1を積む
checked=[0]*(n+1) #各頂点を見たかどうかのフラグを持っておく
while q:
 v=q.pop()
 checked[v]=1 #頂点を見たかどうかのフラグを更新する
 for u in g[v]:
   cnt[u]+=cnt[v]
   q.append(u) #スタックに子ノードuを積む
print(*cnt[1:]) #各頂点のcountが答えとなる


from collections import deque #dfs

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    edges.append([a, b])
ans = 0
for edge in edges:
    q = deque()
    q.append(1)
    checked = [False]*(n+1)
    g[edge[0]].remove(edge[1])
    g[edge[1]].remove(edge[0])
    while q:
        v = q.pop()
        checked[v] = True 
        for u in g[v]:
            if checked[u]:
                continue
            q.append(u) 
    if False not in checked[1:]:
        ans += 1
    g[edge[0]].append(edge[1])
    g[edge[1]].append(edge[0])
print(m - ans)