from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]
INF = 0xffffffff
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cost = [[INF] * w for i in range(h)]
cost[0][0] = 0
q = deque([(0, 0)])

while q:
  x, y = q.popleft()
  c2 = cost[y][x] + 1
  for i in range(4):
    x2 = x + dx[i]
    y2 = y + dy[i]
    if x2 < 0 or x2 >= w  or y2 < 0 or y2 >= h or s[y2][x2] == "#":
      continue
    if cost[y2][x2] > c2:
      cost[y2][x2] = c2
      q.append((x2, y2))
ans = cost[h-1][w-1]




from collections import deque
H, W = map(int, input().split())
G = [list(input()) for i in range(H)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 
ans = 0
for sh in range(H):
    for sw in range(W):
        # 通れないマスはスタートになり得ない
        if G[sh][sw] == '#':
            continue
 
        # BFS
        dist = [[-1] * W for i in range(H)]
        dist[sh][sw] = 0
        que = deque([[sh, sw]])
 
        while que:
            nh, nw = que.pop()
            for dh, dw in directions:
                # 迷路からはみ出す
                if not ((0 <= nh + dh < H) and (0 <= nw + dw < W)):
                    continue
 
                # 移動先が通れないマス
                if G[nh + dh][nw + dw] == '#':
                    continue
 
                # 探索済み
                if dist[nh + dh][nw + dw] != -1:
                    continue
 
                dist[nh + dh][nw + dw] = dist[nh][nw] + 1
                que.appendleft([nh + dh, nw + dw])
        print(dist)
        ans = max(ans, max([max(d) for d in dist]))
 
print(ans)