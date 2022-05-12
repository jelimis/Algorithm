def solution(name):
    answer = 0
    # 기본 최소 이동횟수는 길이의 -1
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        # 조이스틱을 다음 또는 이전 알파벳으로 이동가능하기 때문에
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 왼쪽 or 오른쪽 어느 방향으로 이동? 연속된 A가 많다면 스틱을 이동하지 않을 수 있다.
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교
        min_move = min(min_move, i + i + len(name) - next, i + 2 * (len(name) - next))

    answer += min_move
    return answer