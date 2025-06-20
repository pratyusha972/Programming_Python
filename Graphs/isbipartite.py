n = len(graph)
vis = [-1 for i in range(n)]
flag = True

def dfs(node, vis, color, graph):
    if vis[node] != -1:
        if vis[node] != color:
            return False
        elif vis[node] == color:
            return True
    vis[node] = color
    for n in graph[node]:
       if not dfs(n, vis, not color, graph):
            return False
    return True


for i in range(n):
    if vis[i] == -1:
        if not dfs(i, vis, 0, graph):
            flag = False
            break
print(flag)
