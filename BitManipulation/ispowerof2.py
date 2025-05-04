#Problem:https://leetcode.com/problems/power-of-two/
n = 8
#bit manipulation
if n > 0 and n & (n-1) == 0:
    print(True)
else:
    print(False)
#Method2 
#flag = True
#if n < 1:
#    flag = False
#else:
#    while n > 1:
#        if n%2 == 1:
#            flag = False
#            break
#        n = n//2
#print(flag)
