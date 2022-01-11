from collections import Counter
from operator import itemgetter
n, k = map(int, input().split())
a = Counter(map(int, input().split()))
sa = sorted(a.items(), key=itemgetter(1), reverse=True)