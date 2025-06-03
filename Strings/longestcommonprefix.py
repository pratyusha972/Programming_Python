strs = ["ab", "a"]
if len(strs) == 1:
    print(strs[0])
else:
    minlen = 201
    for i in range(len(strs)):
        templen = len(strs[i])
        minlen = min(minlen, templen)
    i = None
    flag = True
    for i in range(minlen):
        base = strs[0][i]
        for j in range(1, len(strs)):
            if base != strs[j][i]:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(strs[0][:minlen])
    else:
        print(strs[0][:i])
