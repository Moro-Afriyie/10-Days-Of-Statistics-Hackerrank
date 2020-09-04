from math import factorial


def binomial_distribution(x, n, p):
    '''

    :param x: number of success
    :param n: total number of trials
    :param p: probability of success
    :return: binomial probability
    '''
    return (factorial(n)/(factorial(x)*factorial(n-x)))*(p**x)*((1-p)**(n-x))

a, b = list(map(float, input().split()))
# a = 1.09
# b = 1
p = a/(a+b)
print('{:.3f}'.format(sum([binomial_distribution(i, 6, p) for i in range(3, 7)])))
