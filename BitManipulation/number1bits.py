#Problem:https://leetcode.com/problems/number-of-1-bits/
count = 0
n = 11
while n >= 1:
    count += n%2
    n = n//2
print(count)
