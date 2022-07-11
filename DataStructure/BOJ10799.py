s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':  # 여는 괄호라면
        stack.append(s[i])  # 스택에 쌓아준다.
    else:
        stack.pop()  # 닫는 괄호가 나오면 무조건 꺼내준다.
        if s[-1] == '(':
            cnt += len(s)
        else:
            cnt += 1  # 막대기의 마지막 조각들을 더한다.

print(cnt)