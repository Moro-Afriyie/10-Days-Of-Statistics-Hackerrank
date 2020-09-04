n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
rank_x = {sorted(X)[i]: i+1 for i in range(0, len(X))}
rank_y = {sorted(Y)[i]: i+1 for i in range(0, len(Y))}
diff = sum(list(map(lambda x: x ** 2, [rank_x[a] - rank_y[b] for a, b in zip(X, Y)])))
print('{:.3f}'.format(1-(6*diff/(n**3 - n))))

