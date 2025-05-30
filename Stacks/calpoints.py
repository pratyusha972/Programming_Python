#Problem: https://leetcode.com/problems/baseball-game/
from collections import deque
operations = ["5","2","C","D","+"]
d = deque()
for i in range(len(operations)):
    if operations[i] == "C":
        pop = d.pop()
    elif operations[i] == "D":
        d.append(d[-1]*2)
    elif operations[i] == "+":
        d.append(d[-1] + d[-2])
    else:
        d.append(int(operations[i]))
print(sum(d))
