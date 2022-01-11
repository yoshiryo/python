import math

n = int(input())
l = int(math.sqrt(n))
ans = 10
for i in range(1, l+1):
    if n%i == 0:
        a = i
        b = n//i
        a_digits = len(str(abs(a)))
        b_digits = len(str(abs(b)))  
        ma = max(a_digits, b_digits)
        ans = min(ans, ma)
print(ans)