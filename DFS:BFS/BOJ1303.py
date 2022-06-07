import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = []
w = []
b = []

def dfs(x, y, cnt, str):
    arr[x][y] = 'C'
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == str:
            arr[nx][ny] = 'C'
            cnt = dfs(nx, ny, cnt + 1, str)
    return cnt

for _ in range(m):
    arr.append(list(input()))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W':
            result = dfs(i, j, 1, 'W')
            w.append(result * result)
        if arr[i][j] == 'B':
            result = dfs(i, j, 1, 'B')
            b.append(result * result)

print(sum(w))
print(sum(b))