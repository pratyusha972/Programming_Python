n = 10
#Iterate over every number
# def getbin(num):
#     count = 0
#     while num > 0:
#         count += num%2
#         num = num//2
#     return count
#Use the previous calculations
ans = [0]
for i in range(1,n+1):
    ans.append(ans[i//2] + i%2)
print(ans)
