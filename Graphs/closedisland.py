grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
count = 0
def dfs(x, y):
    global m, n, grid
    directions = [(0,1), (0, -1), (1,0), (-1,0)]
    grid[x][y] = 1
    for (dx, dy) in directions:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 0:
            dfs(nx, ny)
    return 

m = len(grid)
n = len(grid[0])
for i in range(n):
    if grid[0][i] == 0:
        dfs(0, i)
    if grid[m-1][i] == 0:
        dfs(m-1, i)

for i in range(m):
    if grid[i][0] == 0:
        dfs(i, 0)
    if grid[i][n-1] == 0:
        dfs(i, n-1)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)  
