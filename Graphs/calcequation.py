from collections import defaultdict
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
s = set()
adj = defaultdict(list)
for i in range(len(equations)):
    adj[equations[i][0]].append((equations[i][1], values[i]))
    adj[equations[i][1]].append((equations[i][0], 1/values[i]))
    s.add(equations[i][0])
    s.add(equations[i][1])

def dfs(node1, node2, adj, vis, val, minweight):
    vis[node1] = True
    flag = False
    for node, weight in adj[node1]:
        if vis[node] == True:
            continue
        if node == node2:
            tempval = val * weight
            minweight = min(minweight, tempval)
            flag = True
        else:
            tempval, tempflag = dfs(node, node2, adj, vis, val*weight, minweight)
            if tempflag == True:
                minweight = min(minweight, tempval)
                flag = tempflag
    return minweight, flag

ans = []
for p, q in queries:
    if p not in s or q not in s:
        ans.append(-1.0)
    elif p == q:
        ans.append(1.0)
    else: 
        vis = {i:0 for i in s} 
        val, flag = dfs(p, q, adj, vis, 1, 10000)
        if flag == False or val == 10000:
            ans.append(-1.0)
        else:
            ans.append(val)
print(ans)
