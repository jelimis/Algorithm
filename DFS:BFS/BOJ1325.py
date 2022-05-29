# 메모리초과에 유의해서 풀어야한다.
# 신뢰하는 방향이 중요하므로 주의해야 한다.

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    # a가 b를 신뢰하니까 b에서 a를 갈 수 있다.
    arr[b].append(a)


def bfs(start):
    visited = [True] * (n + 1)
    q = deque([start])
    cnt = 1
    visited[start] = False
    while q:
        cnt += 1
        now = q.popleft()
        for i in arr[now]:
            if visited[i]:
                visited[i] = False
                q.append(i)
    return cnt


for i in range(1, n + 1):
    answer.append(bfs(i))

max_num = max(answer)
for i in range(n):
    if max_num == answer[i]:
        print(i + 1, end=" ")