n = int(input())
honey = list(map(int, input().split()))
total = sum(honey[:])
result = 0
temp = honey[0]

# 세가지 꿀/벌이 있는 위치를 나눠서 생각해야 한다.

# 벌 - 벌 - 꿀
for i in range(1, n):
    temp += honey[i]  # 중간 벌이 못먹는 꿀의 양
    result = max(result, total - honey[0] + total - temp - honey[i])

# 꿀 - 벌 - 벌
honey.reverse()
temp = honey[0]
for i in range(1, n):
    temp += honey[i]
    result = max(result, total - honey[0] + total - temp - honey[i])

# 벌 - 꿀 - 벌
for i in range(1, n):
    result = max(result, total - honey[0] - honey[-1] + honey[i])

print(result)