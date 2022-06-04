from collections import deque

q = deque()

# 최소일수 또는 주변의 토마토를 익힌다는 깊이를 알아야만 알 수 있기 때문에 bfs를 사용해야 한다.
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1 or arr[nx][ny] == -1:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])


n, m = map(int, input().split())
arr = []
result = 0
# 0 안익은토마토 1 익은토마토 -1 없는토마토
for i in range(m):
    arr.append(list(map(int, input().split(' '))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append([i, j])

bfs()

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result - 1)