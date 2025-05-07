#3341. Find Minimum Time to Reach Last Room I
#https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

#example problem
moveTime = [[17,56], [97,80]]
n = len(moveTime)
m = len(moveTime[0])
scores = [[float('inf') for i in range(m)] for j in range(n)]
scores[0][0] = 0
d = []
d.append((0,0,0))
directions = [(0,1), (0,-1), (1,0), (-1,0)]
while len(d) > 0:
    (time, cx, cy) = heapq.heappop(d)
    for (dx, dy) in directions:
        nx, ny = dx + cx, dy + cy
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if moveTime[nx][ny] > time:
                newtime = moveTime[nx][ny] + 1
            else:
                newtime = time + 1
            if newtime < scores[nx][ny]:
                scores[nx][ny] = newtime
                heapq.heappush(d, (newtime, nx, ny))
print(scores[n-1][m-1])
