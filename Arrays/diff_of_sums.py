#Problem: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
sum1 = 0
sum2 = 0
n = 10
m = 3
for i in range(1,n+1):
    if i%m == 0:
        sum2 += i
    else:
        sum1 += i
print(sum1 - sum2)
