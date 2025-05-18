#Problem: https://leetcode.com/problems/plus-one/
digits = [9, 9, 9]
temp = (digits[-1] + 1)%10
initcarry = (digits[-1] + 1) - 9
digits[-1] = temp
i = len(digits) - 2
while initcarry > 0 and i >= 0:
    temp = (digits[i] + 1)%10
    initcarry = (digits[i] + 1) - 9
    digits[i] = temp
    i -= 1 
if initcarry > 0:
    digits.insert(0, 1)
print(digits)
