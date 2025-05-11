#Problem:https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
haystack = "sadnotsad"
needle = "sad"
ans = haystack.split(needle)
ret = None
if len(ans) == 1:
    ret = -1
else:
    ret = len(ans[0])
print(ret)
