from math import factorial


def binomial_distribution(x, n, p):
    return (factorial(n)/(factorial(x)*factorial(n-x)))*(p**x)*((1-p)**(n-x))

p, n = list(map(float, input().split()))
print('{:.3f}'.format(sum([binomial_distribution(i, n, p/100) for i in range(3)])))  # No more than 2 rejects
print('{:.3f}'.format(1-binomial_distribution(0, n, p/100)-binomial_distribution(1, n, p/100)))  # at least 2 rejects

