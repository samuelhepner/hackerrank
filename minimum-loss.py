# Complete the minimumLoss function below.
def minimumLoss(price):
    diffs = []
    for i in range(len(price)):
        for j in range(len(price)):
            if (i==j):
                pass
            elif (price[i] < price[j]):
                pass
            elif (j < i):
                pass
            else:
                differ = abs(price[i] - price[j])
                diffs.append(differ)

    return min(diffs)

print(minimumLoss([20,7,8,2,5]))
print(minimumLoss([5,10,3]))