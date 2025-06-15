#Problem: https://leetcode.com/problems/number-of-provinces
count = 0
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
def dfs(city, vis, adj):
    vis[city] = True
    for i in range(len(adj[city])):
        if adj[city][i] == 1 and not vis[i]:
            vis = dfs(i, vis, adj)
    return vis

n = len(isConnected)
vis = [False for i in range(n)]
for i in range(n):
    if not vis[i]:
        vis = dfs(i, vis, isConnected)
        count += 1
print(count)
