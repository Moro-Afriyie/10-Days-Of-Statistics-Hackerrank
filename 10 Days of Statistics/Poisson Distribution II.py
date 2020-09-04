# X^2 can be replaced by X + X^2 using the variance formula E[X^2] = X + X^2 
meanA, meanB = list(map(float, input().split()))
Daily_cost_A = 160 + 40*(meanA + meanA**2)
Daily_cost_B = 128 + 40*(meanB + meanB**2)
print('{:.3f}'.format(Daily_cost_A))
print('{:.3f}'.format(Daily_cost_B))