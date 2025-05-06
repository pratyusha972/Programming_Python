#problem:https://leetcode.com/problems/add-binary/
a = "101111"
b = "10"
lena = len(a)
lenb = len(b)
minlen = -1*min(lena, lenb)
if lena > lenb:
    pre = a[:minlen]
elif lena < lenb:
    pre = b[:minlen]
else:
    pre = ""
ans = ""
carry = 0
for i in range(-1, minlen-1, -1):
    temp = int(a[i]) + int(b[i]) + carry
    if temp == 3:
        carry = 1
        ans = "1" + ans
    elif temp == 2:
        carry = 1
        ans = "0" + ans
    elif temp == 1:
        carry = 0
        ans = "1" + ans
    else:
        carry = 0
        ans = "0" + ans
if carry == 0:
    ans = pre + ans
else:
    for i in range(-1, -1*len(pre)-1, -1):
        temp = int(pre[i]) + carry
        if temp == 3:
            carry = 1
            ans = "1" + ans
        elif temp == 2:
            carry = 1
            ans = "0" + ans
        elif temp == 1:
            carry = 0
            ans = "1" + ans
        else:
            carry = 0
            ans = "0" + ans
    if carry > 0:
        ans = "1" + ans
print(ans)
