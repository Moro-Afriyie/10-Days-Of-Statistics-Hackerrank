from statistics import mean, pstdev
# pstdev Return the population standard deviation (the square root of the population variance).
x = int(input())
N = list(map(int, input().split()))
print('{:.1f}'.format(pstdev(N, mean(N))))