import math
import sys

# 입력 속도 최적화를 위해
input = sys.stdin.readline

N, M = map(int, input().split())

# 행렬 A 입력
matrix_A = [list(map(int, input().strip())) for _ in range(N)]

# 행렬 B 입력
matrix_B = [list(map(int, input().strip())) for _ in range(N)]

i = 0
j = 0
def flip(i, j, mat):
    for x in range(i, i+3):
        for y in range(j, j+3):
            mat[x][y] = 1 - mat[x][y]


count = 0
for i in range(N-2):
    for j in range(M-2):
        if matrix_A[i][j] != matrix_B[i][j]:
            flip(i, j, matrix_A)
            count += 1

# 마지막 확인
if matrix_A == matrix_B:
    print(count)
else:
    print(-1)