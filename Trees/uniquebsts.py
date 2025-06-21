n=4
numtrees = [0 for i in range(n+1)]
numtrees[1]=1
numtrees[0]=1
for i in range(2, n+1):
    for j in range(1, i+1):
        numtrees[i] += numtrees[j-1] * numtrees[i-j]
print(numtrees[n])
