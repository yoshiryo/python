import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x:x*(-1), a))

heapq.heapify(a)
ans = 0
for _ in range(m):
    ma = heapq.heappop(a)*(-1)//2
    heapq.heappush(a, -1*ma)
print(sum(a)*(-1))