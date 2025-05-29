#Problem:https://leetcode.com/problems/triangle/
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
for i in range(1, len(triangle)):
    for j in range(1, len(triangle[i])-1):
        triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
    triangle[i][0] += triangle[i-1][0]
    triangle[i][len(triangle[i])-1] += triangle[i-1][-1]
print(min(triangle[-1]))
