#Problem:https://leetcode.com/problems/surrounded-regions/
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
def dfs(x, y):
    global board
    board[x][y] = "P"
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for (dx, dy) in directions:
        nx, ny = dx + x, dy + y
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if board[nx][ny] == "O":
                dfs(nx, ny)
    return

m = len(board)
n = len(board[0])
for i in range(n):
    if board[0][i] == "O":
        dfs(0, i)
    if board[m-1][i] == "O":
        dfs(m-1, i)

for i in range(m):
    if board[i][0] == "O":
        dfs(i, 0)
    if board[i][n-1] == "O":
        dfs(i, n-1)

for i in range(m):
    for j in range(n):
        if board[i][j] == "O":
            board[i][j] = "X"

for i in range(m):
    for j in range(n):
        if board[i][j] == "P":
            board[i][j] = "O"

print(board)
