from statistics import median
'''
quartile is just finding the medians when the array is split into two from the middle
'''
x = int(input())
N = sorted(list(map(int, input().split())))
mid = len(N) // 2
second_quartile = median(N)
if len(N) % 2 == 0:
    first_quartile = median(N[: mid])
    third_quartile = median(N[mid:])
else:
    first_quartile = median(N[: mid])
    third_quartile = median(N[mid + 1:])

print(round(first_quartile))
print(round(second_quartile))
print(round(third_quartile))