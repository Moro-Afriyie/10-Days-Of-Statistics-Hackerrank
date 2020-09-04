from math import sqrt
s = int(input())
mean = int(input())
sd = int(input())
interval = float(input())
z = float(input())
print('{:.2f}'.format(mean - (sd / sqrt(s)) * z, 2))
print('{:.2f}'.format(mean + (sd / sqrt(s)) * z, 2))