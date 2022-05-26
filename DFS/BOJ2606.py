n = int(input())
m = int(input())
array = [[] for _ in range(n+1)]
visited = [True] * (n+1)
cnt = 0

def dfs(start):
  visited[start] = False
  global cnt
  for i in array[start]:
    if visited[i]: # 만약 이미 방문 했다면 하지 않아도 된다.
      cnt += 1 # 방문하지 않은 곳이라면 cnt 1 증가
      dfs(i) # 감연된 컴퓨터에서 감염 된 컴퓨터 개수를 또 찾아야 한다.
  return cnt

for i in range(m):
  x, y = map(int, input().split())
  array[x].append(y)
  array[y].append(x) # 양방향으로 안해주면 오답 왜?

print(array)
print(dfs(1))