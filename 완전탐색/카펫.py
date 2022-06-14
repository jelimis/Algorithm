# 프로그래머스 2단계 완전탐색 카펫
# 가로 a 세로 b 공식을 이용해서 문제풀이

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if 2 * a + 2 * b == brown + 4:
                    return [a, b]
    return answer