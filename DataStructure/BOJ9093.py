import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    s = input().split()
    for i in s:
        print(i[::-1], end=' ') # list[::-1] 문자열 거꾸로 출력!
    print()