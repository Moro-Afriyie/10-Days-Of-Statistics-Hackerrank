import math
def normal_distribution(mean, sd,x):
    '''
    :param mean: mean
    :param sd: standard deviation
    :return: normal distribution probability
    '''
    result = 0.5*(1 + math.erf((x-mean)/(sd*math.sqrt(2))))
    return result


mean, sd = list(map(float, input().split()))
x = float(input())
y, z = list(map(float, input().split()))

print('{:.3f}'.format(normal_distribution(mean, sd, x)))
print('{:.3f}'.format(normal_distribution(mean, sd, z)-normal_distribution(mean, sd, y)))