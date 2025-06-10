from collections import deque
def isvalid(s):
    d = deque()
    d.append("p")
    flag = True
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            d.append(s[i])
        elif (s[i] == ")" and d[-1] == "(") or (s[i] == "]" and d[-1] == "[") or (s[i] == "}" and d[-1] == "{"):
            temp1 = d.pop()
        else:
            flag = False
            break
    if flag == False:
        return flag
    if len(d) == 1 and d[-1] == "p":
        return True
    return False
s = "()"
print(isvalid(s))
