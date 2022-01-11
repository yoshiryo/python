from itertools import product
n, m, x = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
l = list(product([False, True], repeat=n))
mi = 10**5 * 12 + 1

for i in range(len(l)):
    money = 0
    algo = [0]*m
    ans = l[i]
    for j in range(n):
        if ans[j] == True:
            c = a[j]
            money += c[0]
            for k in range(1, m+1):
                algo[k-1] += c[k]
        if min(algo) >= x:
            mi = min(money, mi)
if mi == 10**5 * 12 + 1:
    print(-1)
else:
    print(mi)