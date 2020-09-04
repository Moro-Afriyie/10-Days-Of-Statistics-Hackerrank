from math import factorial


def poisson(k, mean):
    '''
    poission probability the probability of getting exactly k successes when the average number of success or mean is
    given
    :param k: the actual natural number of successes that occur in the specified region
    :param mean: the average number of successes that occur in the specified region or mean
    :return: poisson probability
    '''
    e = 2.71828
    poisson_probability = ((mean**k)*(e**-mean))/factorial(k)
    return poisson_probability

mean = float(input())
k = int(input())
print('{:.3f}'.format(poisson(k, mean)))