import sys
sys.setrecursionlimit(10000)
# 문제 조건을 보고 재귀 깊이를 제한하자

def dfs(x, y, cnt):
  trash[x][y] = 2
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >=n or ny < 0 or ny>=m:
      continue
    if trash[nx][ny] == 1:
      trash[nx][ny] = 2
      cnt = dfs(nx, ny, cnt+1)
  return cnt

n, m, k = map(int, input().split())
result = []
trash = [[0]*m for _ in range(n)]
for _ in range(k):
  x, y = map(int, input().split())
  trash[x-1][y-1] = 1

for i in range(n):
  for j in range(m):
    if trash[i][j] == 1:
      result.append(dfs(i, j, 1))

print(max(result))