#Problem: https://leetcode.com/problems/number-of-islands/
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
count = 0
def dfs(x, y):
    global m, n, grid
    directions = [(0,1), (0, -1), (1,0), (-1,0)]
    grid[x][y] = "0"
    for (dx, dy) in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == "1":
            dfs(nx, ny)
    return 

m = len(grid)
n = len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j] == "1":
            dfs(i, j)
            count += 1
print(count)
