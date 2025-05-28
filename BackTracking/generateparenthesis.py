#Problem:https://leetcode.com/problems/generate-parentheses/
n = 3
ans = []
def recur(n, s, op):
    if n == 0:
        while op>0:
            s += ")"
            op-=1
        ans.append(s)
        return
    for i in range(op+1):
        recur(n-1, s+")"*i+"(", op + 1 - i)
    return
recur(n, "", 0)
print(ans)
