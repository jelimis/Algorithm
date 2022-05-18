def solution(number, k):
    answer = []  # 스택으로 풀이하면 시간초과 문제를 해결할 수 있다.

    for num in number:
        # k만큼 제거해줘야 하니까
        # 현재 answer의 값이 number보다 작으면 answer값 제거해준다.
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        # 처음에 아무것도 없을 때, answer값 num값 추가
        answer.append(num)
    return ''.join(answer[:len(answer)])