from statistics import mean, pstdev
'''
Y = a + bX
b = PearsonCorrelationCoefficient * (sd(Y)/(sd(X))
a = mean(y) - b*(mean(x))
'''
def P(X, Y,n):
    covariance = [(i - mean(X)) * (j - mean(Y)) for i, j in zip(X, Y)]
    pearson_correlation = sum(covariance) / (n * pstdev(X, mean(X)) * pstdev(Y, mean(Y)))
    return pearson_correlation


X = []
Y = []
for i in range(5):
    m = list(map(int, input().split()))
    X.append(m[0])
    Y.append(m[1])
b = P(X, Y, 5)*(pstdev(Y, mean(Y)) / (X, mean(X)))
a = mean(Y) - b*mean(X)
# at x = 80
print('{:.3f}'.format(a + b*80))
