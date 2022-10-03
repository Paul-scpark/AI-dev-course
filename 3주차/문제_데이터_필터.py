# 데이터 필터 문제

### 체감 난이도: 2
### numpy - reshape, append 함수 활용

import numpy as np

def solution(data, data_filter):
    
    res = np.array([])
    
    # 주어진 각각의 data 배열에 대하여 data의 길이만큼 data_filter 값을 나눈 배열을 np.dot 해주기
    for i in data:
        res = np.append(res, np.dot(i, data_filter / len(data)))
    
    # 최종적인 return 값의 shape은 (data의 길이, data_filter의 shape) 형태이므로 이에 맞게 reshape
    return res.reshape(len(data), data_filter.shape[0], data_filter.shape[1])