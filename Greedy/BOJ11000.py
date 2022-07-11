# 시간초과 조건을 생각하지 않고 문제풀이를 했더니 오답

N = int(input())
arr = []

for i in range(N):
    S, T = map(int, input().split())
    arr.append([S, T])

arr.sort(key=lambda x: (x[1], x[0]))
check = [True] * N
result = 0

while True:
    if check.count(True) == 0:
        break

    str = check.index(True)
    next = arr[str][1]
    check[str] = False

    for i in range(N):
        if next <= arr[i][0] and check[i]:
            next = arr[i][1]
            check[i] = False
    result += 1

print(result)

# 리스트를 추가/제거할 때에는 heapq를 사용하자!
import heapq

N = int(input())
arr = []
heap = []

for i in range(N):
    S, T = map(int, input().split())
    arr.append([S, T])

arr.sort(key=lambda x: x[0])
heapq.heappush(heap, arr[0][1])
# 첫번째 강의가 끝나는 시간을 넣는다.

for i in range(1, N):
    if heap[0] > arr[i][0]: # 만약 앞에 끝나는 시간이 뒤에 시작시간보다 크다면 방을 하나 더 만들어준다.
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap) # 같거나 작다면 현재 리스트에서 제거하고
        heapq.heappush(heap, arr[i][1]) # 현재 끝나는 시간으로 변경한다.

print(len(heap))