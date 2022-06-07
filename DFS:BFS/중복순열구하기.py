def DFS(L):
global cnt
if L == m:
  for j in rnage(m):
    print(a[j], end=' ')
  print()
  cnt +=1
else:
  for i in range(1, n+1):
    a[L] = i
    DFS(L+1)
n, m = map(int, input().split())

a = [0]*n
cnt = 0
for _ in range(N):
  DFS(0)
  print(cnt)