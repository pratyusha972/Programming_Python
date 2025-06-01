#Problem: https://leetcode.com/problems/accounts-merge/
from collections import defaultdict
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
adj = defaultdict(list)
d = {}
for account in accounts:
    name = account[0]
    if len(account) == 2:
        d[account[1]] = name
        if account[1] not in adj.keys():
            adj[account[1]] = []
    else:
        for i in range(1, len(account)):
            d[account[i]] = name
            for j in range(i+1, len(account)):
                adj[account[i]].append(account[j])
                adj[account[j]].append(account[i])

def find(x, parent):
    if parent[x] != x:
        parent[x], parent = find(parent[x], parent)
    return parent[x], parent

def union(n1, n2, parent):
    r1, parent = find(n1, parent)
    r2, parent = find(n2, parent)
    if r1 == r2:
        return parent
    parent[r2] = r1
    return parent

l = list(adj.keys())
d2 = {}
for i in range(len(l)):
    d2[l[i]] = i
parent = {i:i for i in range(len(l))}
for node in l:
    for conn in adj[node]:
        parent = union(d2[node], d2[conn], parent)

ans = []
d1 = defaultdict(list)
for i in range(len(parent)):
    temp = i
    while parent[temp]!=temp:
        temp = parent[temp]
    parent[i] = temp
    d1[parent[i]].append(l[i])

ans = []
for key, val in d1.items():
    temp = []
    temp.append(d[val[0]])
    temp.extend(sorted(val))
    ans.append(temp)            

print(ans)
