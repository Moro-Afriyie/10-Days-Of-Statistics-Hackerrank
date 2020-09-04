import math
'''
The central limit theorem (CLT) states that, for a large enough sample (), the distribution of the sample mean will
 approach normal distribution. This holds for a sample of independent random variables from any distribution with 
 a finite standard deviation.
 mu = mu*n
 sd = sd* sqrt(n)
'''
def cdf(mean, sd,x):
    result = 0.5 * (1 + math.erf((x - mean) / (sd * math.sqrt(2))))
    return result


x = int(input())
n = int(input())
mean = float(input())
sd = float(input())

mean_sum = n*mean
sd_sum = math.sqrt(n) * sd

print('{:.4f}'.format(cdf(mean_sum, sd_sum,  x)))