import sys

sys.setrecursionlimit(100000)

m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for i in range(m)]
visited = [[True for _ in range(n)] for i in range(m)]
result = []


def dfs(x, y, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 0 and visited[nx][ny]:
            visited[nx][ny] = False
            cnt = dfs(nx, ny, cnt + 1)
    return cnt

# 나는 왜 직사강형을 만드는 (1로 채우는) 공식을 제대로 이해하지 못했을까..이것만 아니었으면 바로 풀었다.
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j]:
            result.append(dfs(i, j, 1))

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")