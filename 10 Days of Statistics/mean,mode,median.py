import statistics
from collections import Counter
x = int(input())
N = list(map(int, input().split()))
print(statistics.mean(N))
print(statistics.median(N))
print(min([a for a,b in Counter(N).items() if b == max(Counter(N).values())]))