from statistics import pstdev, mean


def P(X, Y,n):
    covariance = [(i - mean(X)) * (j - mean(Y)) for i, j in zip(X, Y)]
    pearson_correlation = sum(covariance) / (n * pstdev(X, mean(X)) * pstdev(Y, mean(Y)))
    return pearson_correlation


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
print('{:.3f}'.format(P(X, Y, n)))


