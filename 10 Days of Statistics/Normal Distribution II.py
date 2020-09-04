import math
def normal_distribution(mean, sd,x):
    return 0.5*(1 + math.erf((x-mean)/(sd*math.sqrt(2))))

mean, sd = list(map(float, input().split()))
x = float(input())
y = float(input())
print('{:.2f}'.format((1-normal_distribution(mean, sd, x))*100))  # higher than 80
print('{:.2f}'.format((1-normal_distribution(mean, sd, y))*100))   # greater than or equal to 60
print('{:.2f}'.format(normal_distribution(mean, sd, y)*100))   # less than o 60
