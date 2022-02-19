#ある数列の部分列(1<=L<=R<=N を満たすL~R)の和を足した時の値を求めるもの
n = int(input())
a = list(map(int, input().split()))
mod = 998244353
b = [0]
cnt = 0
for i in range(n): #累積和を求める
    cnt += a[i]
    b.append(cnt)
b.sort() #sortする
ans = 0
for i in range(n+1): #(2*i - n)*b[i]の和で求めることができる
    ans += (2*i - n)*b[i]
    ans %= mod
print(ans)