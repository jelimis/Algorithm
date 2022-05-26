from collections import deque

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [True] * (n+1)

for i in range(m):
  x, y = map(int, input().split())
  arr[x].append(y)
  arr[y].append(x)

for i in range(len(arr)):
  arr[i].sort()

def dfs(start):
  print(start, end=" ")
  visited[start] = False # 정점을 지나갔다는 표시
  for i in arr[start]: # 현재 정점에 연결되어 있는 정점들을 지나간다.
    if visited[i]:
      visited[i] = False
      dfs(i) # 지금 정점에서 연결되어있는 모든 정점 먼저 체크한다.

dfs(v)
print()

visited = [True] * (n+1) # dfs 함수를 이용해서

def bfs(start):
  q = deque([start]) # 시작점 queue에 담는다.
  visited[start] = False
  while q:
    now = q.popleft() # 첫번째 queue 꺼낸다.
    print(now, end=' ')
    for i in arr[now]:
      if visited[i]:
        visited[i] = False
        q.append(i)

bfs(v)
