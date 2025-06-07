#Problem:https://leetcode.com/problems/asteroid-collision/
l = []
asteroids = [5,10,-5]
for i in range(len(asteroids)):
    if asteroids[i] >= 0:
        l.append(asteroids[i])
    else:
        length = len(l)
        if length == 0 or (length > 0 and l[-1] < 0):
            l.append(asteroids[i])
        else:
            temp = abs(asteroids[i])
            top = 10000
            while len(l) > 0 and l[-1] >= 0 and l[-1] < temp:
                top = l.pop()
            if len(l) > 0 and l[-1] == temp:
                top = l.pop()
            elif top < temp and (len(l) == 0 or (len(l) > 0 and l[-1] < 0)):
                l.append(asteroids[i])
print(l)
