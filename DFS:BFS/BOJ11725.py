# 정답은 맞는데 메모리초과 / 블로그 답안지 참고해도 메모리 초과

import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(arr, start, visited):
  visited[start] = False # 방문한 노드는 False
  for i in arr[start]:
    if visited[i]:
      answer[i] = start
      dfs(arr, i, visited)

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [True] * (n+1)
answer = [0] * (n+1)

for i in range(n-1):
  x, y = map(int, input().split())
  arr[x].append(y)
  arr[y].append(x)

dfs(arr, 1, visited)

for i in range(2, n+1):
  print(answer[i])