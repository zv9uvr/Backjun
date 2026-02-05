import math
import sys
from collections import deque

# 입력 속도 최적화를 위해
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 방의 세로 길이, M: 방의 가로 길이
r, c, d = map(int, input().split()) # (r, c): 처음 로봇 청소기의 위치
                                    # d: 처음에 로봇 청소기가 바라보는 위치
                                    # ( 북:0 | 동:1 | 남:2 | 서:3 )

room = [list(map(int, input().split())) for _ in range(N)]

# 북(0), 동(1), 남(2), 서(3) 기준 이동 변화량
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
            
num = 0 # 청소하는 칸의 개수

while True:    
    # 1) 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[r][c] == 0: # 만약 해당 칸이 청소되지 않았다면
        room[r][c] = 2  # 2: 청소된 칸
        num += 1    # 청소한 칸의 개수 1 증가
    
    found_blank = False
    # 주변 4칸 탐색
    for _ in range(4):
        d = (d+3) % 4   # 반시계 90도 회전 및 값 업데이트
        nr, nc = r + dr[d], c + dc[d]
        
        # 방 범위 안이고, 청소되지 않은 빈칸(0)인 경우
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            found_blank = True
            break # 전진했으므로 1번으로 돌아감
    
    # 2. 주변 4칸 중 빈칸이 없는 경우
    if not found_blank:
        # 바라보는 방향 유지하며 한 칸 후진
        br, bc = r - dr[d], c - dc[d]
        
        # 후진 가능 여부 체크 (벽이 아니면 후진)
        if 0 <= br < N and 0 <= bc < M and room[br][bc] != 1:
            r, c = br, bc
        else:
            break # 뒤가 벽이면 작동 멈춤
        
print(num)
