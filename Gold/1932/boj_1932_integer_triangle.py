import math
import sys

# 입력 속도 최적화를 위해
input = sys.stdin.readline

N = int(input())    # 삼각형의 크기 N

integer = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, N):   # 2번째 줄부터 시작
    for j in range(len(integer[i])):
        # 맨 왼쪽일 때
        if j == 0:
            integer[i][j] += integer[i-1][j]
        # 맨 오른쪽일 때
        elif j == i:
            integer[i][j] += integer[i-1][j-1]
        # 가운데 끼어있을 때
        else:
            integer[i][j] += max(integer[i-1][j-1], integer[i-1][j])

print(max(integer[N-1]))