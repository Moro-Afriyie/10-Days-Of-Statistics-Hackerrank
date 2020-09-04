'''
The interquartile range of an array is the difference between its first  and third  quartiles
'''
from statistics import median
n = int(input())
X = list(map(int, input().split()))
f = list(map(int, input().split()))
s = sorted([a for a, b in zip(X, f) for i in range(b)])
mid = len(s) // 2
if len(s) % 2 == 0:
    first_quartile = median(s[: mid])
    third_quartile = median(s[mid:])
else:
    first_quartile = median(s[: mid])
    third_quartile = median(s[mid + 1:])
print('{:.1f}'.format(third_quartile - first_quartile))
