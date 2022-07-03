A, B = map(int, input().split())
result = 1

while True:
  if B == A:
    break
  elif (B % 2 != 0 and B % 10 != 1) or (B < A):
    # 맨 뒷자리가 1로 나누어지지 않거나 뒷자리가 1이 아니라면 더이상 진행할 수 없다.
    result = -1
    break
  else:
    if B % 2 == 0:
      B //= 2
      result += 1
    elif B % 10 == 1:
      B //= 10
      result += 1

print(result)