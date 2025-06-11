#Problem: https://takeuforward.org/plus/dsa/problems/best-time-to-buy-and-sell-stock
arr = [10, 7, 5, 8, 11, 9]
min_i = arr[0]
profit = 0
for i in range(len(arr)):
    profit = max(profit, arr[i] - min_i)
    min_i = min(min_i, arr[i])
print(profit)
