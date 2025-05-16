#Problem:https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
boxes = "110"
ans = []
pre_count = 0
pre_sum = 0
suf_count = 0
suf_sum = 0
for i in range(len(boxes)):
    ans.append(pre_count*i - pre_sum)
    if boxes[i] == "1":
        pre_count += 1
        pre_sum += i
for i in range(len(boxes)-1, -1, -1):
    ans[i] += suf_sum - suf_count * i
    if boxes[i] == "1":
        suf_count += 1
        suf_sum += i
print(ans)
