# 롤러코스터 문제

### 체감 난이도: 1
### numpy - where 함수 활용, where 함수의 multiple conditions, set 활용

import numpy as np

def solution(info):
    ### [풀이 1] - for 반복문 없이 numpy 활용으로 문제 풀이
    height = np.where((info[0] > 195) | (info[0] < 150))
    weight = np.where(info[1] >= 140)
    
    # 중복된 항목들은 set 함수로 제거해주기
    return sorted(list(set(height[0].tolist() + weight[0].tolist())))

    ### [풀이 2] - for 반복문 활용하여 조건에 맞는 인덱스 찾기 문제 풀이
    # answer = []
    # for i in range(len(info[0])):
    #     if info[0][i] < 150 or info[0][i] > 195 or info[1][i] >= 140:
    #         answer.append(i)
    # return answer