'''
The problem is to find P(X <= 5). So we have to do this: P(1) + P(2) + P(3) + P(4) + P(5).
This is a pretty bad thing to do since if it was say P(X <= 1000) a lot of calculations needed to be done.
Lets, approach the problem in a simpler way. First we find P(X > 5), i.e, a defect is found after the first 5 trials,
 i.e, the first 5 DID NOT have any defect. Which is basically (1 - p)^5. Now P(X <= 5) is the complement of P(X > 5)
 which leads us to (1 - P(X > 5)), this saves us a lot computations.
'''
def geometric_distributon(n, p):
    return ((1-p)**(n-1))*p


a, b = list(map(int, input().split()))
n = int(input())
print(round(1 - (1 - (a / b))**n, 3))  # using the complement rule
print('{:.3f}'.format(sum([geometric_distributon(i, a/b) for i in range(1, n+1)]))) # using the normal method
