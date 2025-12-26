import itertools
import math


T = int(input())  # 테스트 케이스 수

value_list = []

# 2개를 뽑는 조합 출력
for test_case in range(T):
    N = int(input())  # 집합 P의 점의 개수
    points = [tuple(map(int, input().split())) for _ in range(N)]  # 각 집합의 점 좌표 입력받기
    total_x = sum(p[0] for p in points)
    total_y = sum(p[1] for p in points)
    
    min_length = float('inf')
    for minus_points in itertools.combinations(points, N // 2):
        # 선택된 시작점들의 합
        sum_minus_x = sum(p[0] for p in minus_points)
        sum_minus_y = sum(p[1] for p in minus_points)
        
        # 끝점들의 합 = (전체 합 - 시작점들의 합)
        # 최종 벡터 X = (끝점 합) - (시작점 합) 
        #            = (total_x - sum_minus_x) - sum_minus_x
        final_x = total_x - 2 * sum_minus_x
        final_y = total_y - 2 * sum_minus_y
        
        # 3. 최종 벡터의 길이 계산
        length = math.sqrt(final_x**2 + final_y**2)
        min_length = min(min_length, length)

    value_list.append(min_length)

for value in value_list:
    print(value)


