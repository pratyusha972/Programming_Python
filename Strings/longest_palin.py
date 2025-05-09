#Problem: https://leetcode.com/problems/longest-palindromic-substring/description/
#example
s = "ccc"
if len(s) == 0:
    ans = ""
else:
    maxlen = 1
    l = len(s)
    ans= ""
    for i in range(l):
        left = i-1
        right = i+1
        templen = 1
        while left >=0 and right < l:
            if s[left] == s[right]:
                templen += 2
                if templen > maxlen:
                    ans = s[left:right+1]
                    maxlen = templen
                left -= 1
                right += 1
            else:
                break
        left = i
        right = i+1
        templen = 0
        while left >=0 and right < l:
            if s[left] == s[right]:
                templen += 2
                if templen > maxlen:
                    ans = s[left:right+1]
                    maxlen = templen
                left -= 1
                right += 1
            else:
                break
    if maxlen == 1:
        ans = s[0]
print(ans)
