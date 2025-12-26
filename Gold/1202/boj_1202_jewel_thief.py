import math
import heapq
import sys

# 입력 속도 최적화를 위해
input = sys.stdin.readline

N, K = map(int, input().split())    # 보석상에 있는 보석의 개수 N, 도둑이 가지고 있는 가방의 개수 K

jewels = [tuple(map(int, input().split())) for _ in range(N)]   # 각 보석의 무게(Mi), 가격(Vi)

# 보석들을 무게(Mi)는 오름차순, 가격(Vi)은 내림차순으로 정렬
jewels.sort(key=lambda x:(x[0], -x[1]))

Ci = []
for i in range(K):
    Ci.append(int(input()))
    
# 최대 가방 무게(Ci)를 오름차순으로 정렬
Ci.sort()

# 우선순위 큐 자료구조를 활용하여 훔칠 수 있는 보석 가격의 합의 최댓값 계산
temp_jewels = []
total_value = 0
j_idx = 0

# 핵심 로직
for bag_limit in Ci:
    # 현재 가방에 담을 수 있는 모든 보석을 힙에 추가
    while j_idx < N and jewels[j_idx][0] <= bag_limit:
        # 최대 힙을 위해 가치에 마이너스(-)를 붙여 push
        heapq.heappush(temp_jewels, -jewels[j_idx][1])
        j_idx += 1
        
    # 가방 하나당 가장 비싼 보석 하나만 담기
    if temp_jewels:
        total_value -= heapq.heappop(temp_jewels)

print(total_value)

