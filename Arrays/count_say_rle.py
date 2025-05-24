#Problem: https://leetcode.com/problems/count-and-say/
def rle(s):
    if s == "1":
        return "11"
    count = 1
    news = ""
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            news += str(count) + s[i-1]
            count = 1
    news += str(count) + s[len(s)-1]
    return news

n = 10
if n == 1:
    print("1")
else:
    temp = "1"
    while n > 1:
        temp = rle(temp)
        n-=1
    print(temp)
