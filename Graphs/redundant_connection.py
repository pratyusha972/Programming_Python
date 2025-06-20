#Problem: https://leetcode.com/problems/redundant-connection
#union find
edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
n = len(edges)
parent = {i:i for i in range(1, n+1)}

def find(node, parent):
    if parent[node] != node:
        parent[node], parent = find(parent[node], parent)
    return parent[node], parent

ans = False
for (n1, n2) in edges:
    root1, parent = find(n1, parent)
    root2, parent = find(n2, parent)
    if root1 == root2:
        ans = [n1, n2]
    else:
        parent[root2] = root1

print(ans)
