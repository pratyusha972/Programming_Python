#Oriblem: https://leetcode.com/problems/score-of-a-string/
s = "hello"
count = 0
for i in range(1, len(s)):
    count += abs(ord(s[i]) - ord(s[i-1]))
print(count)
