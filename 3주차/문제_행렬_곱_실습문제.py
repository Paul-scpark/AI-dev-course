# 행렬 곱 실습문제

### 체감 난이도: 1
### numpy - shape 함수, dot 함수 활용

import numpy as np

def solution(arr_list):
    # 주어진 조건에 따라 A 배열을 정의
    A = np.array([[0]])
    
    # 행렬 곱이 가능한 상태 일 때, A 배열을 업데이트
    for i in arr_list:
        if np.shape(A)[1] == np.shape(i)[0]:
            A = np.dot((A + 1), (i * 2))
    return A