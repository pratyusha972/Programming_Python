#Problem:https://leetcode.com/problems/find-words-containing-character/
words = ["leet","code"]
x = "e"
ans = []
for i in range(len(words)):
    if x in words[i]:
        ans.append(i)
print(ans)
