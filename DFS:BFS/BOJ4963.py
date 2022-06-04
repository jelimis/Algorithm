import sys
sys.setrecursionlimit(100000)
# 재귀문제가 발생했을 때 파이썬의 재귀 깊이를 제한해줘야 한다.

def dfs(x, y):
  dx = [-1, 1, 0, 0, -1, -1, 1, 1]
  dy = [0, 0, -1, 1, -1, 1, -1, 1]
  visited[x][y] = False
  for k in range(8):
    nx = x + dx[k]
    ny = y + dy[k]
    if nx < 0 or nx >= h or ny < 0 or ny >= w:
      continue
    if arr[nx][ny] == 1 and visited[nx][ny]:
      visited[nx][ny] = False
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  arr = []
  cnt = 0
  for k in range(h):
    tmp = list(map(int,input().split(' ')))
    arr.append(tmp)
  visited = [[True for i in range(w)]for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if arr[i][j] == 1 and visited[i][j]:
        cnt += 1
        dfs(i, j)
  print(cnt)