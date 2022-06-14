# 인프런 회의실 배정 그리디
# 그리디는 정렬 기준을 정하는 것이 중요하다.

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr = sorted(arr, key=lambda x: (x[1], x[0]))

result = 1
tmp = arr[0][1]
for i in range(1, n):
    if arr[i][0] >= tmp:
        result += 1
        tmp = arr[i][1]

print(result)