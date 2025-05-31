#Problem:https://leetcode.com/problems/isomorphic-strings/
s = "egg"
t = "add"
d = {}
d2 = {}
flag=True
flag2 = True
for i in range(len(s)):
    if s[i] in d.keys() and t[i]!=d[s[i]]:
        flag = False
        break
    else:
        d[s[i]] = t[i]
for i in range(len(t)):
    if t[i] in d2.keys() and s[i]!=d2[t[i]]:
        flag2 = False
        break
    else:
        d2[t[i]] = s[i]
print(flag and flag2)
