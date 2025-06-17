#Problem: https://leetcode.com/problems/possible-bipartition/
from collections import defaultdict

n = 4
dislikes = [[1,2],[1,3],[2,4]]
vis = [-1 for i in range(n)]
def dfs(node, vis, color, adj):
    if vis[node] != -1:
        if vis[node] == color:
            return True
        return False
    vis[node] = color
    for conn in adj[node]:
        if not dfs(conn, vis, not color, adj):
            return False
    return True

adj = defaultdict(list)
#adj = {i:[] for i in range(len(n))}
for i in range(len(dislikes)):
    adj[dislikes[i][0]-1].append(dislikes[i][1]-1)
    adj[dislikes[i][1]-1].append(dislikes[i][0]-1)

ans = True
for i in range(n):
    if vis[i] == -1:
        if not dfs(i, vis, 0, adj):
            ans = False
            break
print(ans)
