#problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#used sliding window & 2 pointers approaches
s = "abcabcbb"
if s == "":
    ans = 0
else:
    right = 0
    left = 0
    l = len(s)
    a = {}
    ans = 1
    prev_len = 0
    while right < l:
        if a.get(s[right], -1) >= left:
            left = max(a[s[right]]+1, left)
            prev_len = right - left + 1
        else:
            prev_len += 1
            ans = max(ans, prev_len)
        a[s[right]] = right
        right += 1
print(ans)
