from collections import deque

n = int(input())
arr = []
answer = []
for i in range(n):
    arr.append(list(map(int, input())))

def bfs(a, b):
    q = deque()
    q.append((a, b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    arr[a][b] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for a in answer:
    print(a)