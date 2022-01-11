import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)
c = sorted(c)
ans = 0
for i in b:
    maxp = bisect.bisect_left(a, i)
    minp = bisect.bisect_right(c, i)
    ans += maxp*(n-minp)
print(ans)