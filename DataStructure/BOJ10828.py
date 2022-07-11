n = int(input())
stack = []
result = []

# 바로 print() 함수를 이용하면 시관초과 발생 ?!
# result 리스트에 답을 넣고 출력하면 결과 정답
for i in range(n):
  a = list(input().split(' '))
  if a[0] == 'push':
    stack.append(int(a[1]))
  elif a[0] == 'top':
    if stack:
      result.append(stack[-1])
    else:
      result.append(-1)
  elif a[0] == 'size':
    result.append(len(stack))
  elif a[0] == 'pop':
    if stack:
      result.append(stack.pop())
    else:
      result.append(-1)
  else:
    if stack:
      result.append(0)
    else:
      result.append(1)

for i in result:
  print(i)