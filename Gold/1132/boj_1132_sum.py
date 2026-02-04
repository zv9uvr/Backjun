import math
import sys
import operator
from collections import deque

# 입력 속도 최적화를 위해
input = sys.stdin.readline

N = int(input())
weight_array = [0]*10
alp_array = []  # 결괏값 계산을 위해 모든 문자열 저장

# 각 알파벳 별 가중치 계산
for j in range(N):
    alp = list(input()) # 각 alp(ex. ABC, BCA)를 N번 씩 입력받는다.
    alp = alp[0:len(alp)-1] # 배열에서 개행문자 제거
    alp_array.append(alp)
    for i in range(len(alp)):
        index = ord(alp[i])-65  # A=0, B=1, C=2 ...
        weight = len(alp)-i-1   # 가중치. 10^weight
        weight_array[index]+=(10**weight)

params = {} # key: 알파벳, value: 각 알파벳의 가중치
keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i in range(len(keys)):
    params[keys[i]] = weight_array[i]

# value(각 알파벳의 가중치)를 기준으로 딕셔너리 내림차순 정렬
# 리스트 형식으로 출력
sorted_params = sorted(params.items(), key=operator.itemgetter(1), reverse = True)

op_keys = [item[0] for item in sorted_params]   # 가중치가 큰 순으로 정렬된 알파벳만 리스트로 뽑아내기

# 조건 반영 방법: op_keys에서 시작하는 숫자가 아닌 알파벳을 맨 뒤로 보내기
start_num = []  # 시작하는 숫자
for i in range(N):
    temp = []   # 임시 배열
    start = alp_array[i][0]
    start_num.append(start)
   # if alp_array[i][0] == op_keys[len(op_keys)-1]:

missing = [item for item in op_keys if item not in start_num]   # 시작하는 수가 아닌 알파벳

temp = []   # 임시 배열
for i in range(N):
    if alp_array[i][0] == op_keys[len(op_keys)-1]:  # 만약 가중치가 가장 낮은 알파벳이 시작 수 알파벳이라면
        # 시작수가 아닌 알파벳(missing) 중에서 가중치가 가장 낮은 알파벳을 op_keys의 맨 마지막으로 보낸다.
        last_num = op_keys.index(missing[len(missing)-1])  # 가중치 가장 낮은 알파벳의 index 번호
        dq = deque(op_keys[last_num:len(op_keys)])
        dq.rotate(-1)
        new = list(dq)
        for i in range(last_num):
            temp.append(op_keys[i])
        for i in range(len(new)):
            temp.append(new[i])

        op_keys = temp


operands = {}   # key: 가중치 순으로 정렬된 알파벳, value: 각 알파벳에 해당되는 값
values = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(op_keys)):
    operands[op_keys[i]] = values[i]

result = 0  # 결과값

for i in range(N):
    squared_num = len(alp_array[i])-1   # 자릿수를 위해. 
                                        # ABC -> A: 10^2 자릿수 -> squared_num = len(alp_array[i])-1
    for j in range(len(alp_array[i])):
        result += (10**squared_num)*operands[alp_array[i][j]]   # alp_array[i][j] = i번째 줄 문자열의 j번째 문자
        squared_num-=1  # 1씩 빼면서 차수 낮추기

print(result)
