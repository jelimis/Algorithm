from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input()))) #문제에서 받아야하는 리스트값 입력 받는 방법 잘 복습하기

def bfs(a, b):
    q = deque()
    q.append((a, b)) # x,y 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 0:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1 # 이전에 지나왔던 거리를 계속해서 더해준다.
                q.append((nx, ny))  # 새로운 nx, ny를 큐에 추가한다.

    return arr[n - 1][m - 1] # 마지막 좌표를 반환해야 하니까!

print(bfs(0, 0))