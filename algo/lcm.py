import functools
def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def gcd(nums):#最大公約数(複数)
    return functools.reduce(euclid, nums)

def multiple(a, b):#最小公倍数(2つ)
    return a*b // euclid(a, b) 

def lcm(nums):#最初公倍数(複数)
    return functools.reduce(multiple, nums)

def make_divisors(n): #約数列挙
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]