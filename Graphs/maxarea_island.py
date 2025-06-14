grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def dfs(i, j, area):
    global grid, m, n
    grid[i][j] = 0
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = dx + i, dy + j
        if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1:
            area = dfs(nx, ny, area + 1)
    return area

maxarea = 0
m = len(grid)
n = len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            maxarea = max(dfs(i, j, 1), maxarea)

print(maxarea)
