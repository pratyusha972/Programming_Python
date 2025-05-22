#Problem:https://leetcode.com/problems/first-bad-version/
def isbad(num):
    if num >= 4:
        return True
    else:
        return False
bad = 4
n = 5
left = 1
right = n
while left < right:
    mid = left + (right-left)//2
    if isbad(mid) == False:
        left = mid + 1
    else:
        right = mid
print(left) 
