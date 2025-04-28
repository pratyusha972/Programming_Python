#Problem:https://leetcode.com/problems/unique-paths/
m = 3
n = 2
##Dynamic programming, Time:O(M*N), space:O(M*N)
#dp = [[0 for i in range(n)] for j in range(m)]
#for i in range(n):
#    dp[0][i] = 1
#for i in range(m):
#    dp[i][0] = 1
#for i in range(1, m):
#    for j in range(1, n):
#        dp[i][j] = dp[i-1][j] + dp[i][j-1]
#print(dp[m-1][n-1])

#Space: O(N), Time: O(M*N)
top_row = [1 for i in range(n)]
for i in range(1,m):
    prev_val = 1
    for j in range(1,n):
        top_row[j] = prev_val + top_row[j]
        prev_val = top_row[j]
print(top_row[n-1])
