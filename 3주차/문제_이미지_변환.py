# 이미지 변환 문제

### 체감 난이도: 2
### numpy - reshape, ravel 함수 활용

import numpy as np

def solution(img):

    # 주어진 img 값에 따라 높이와 너비 값을 각각 H, W로 정의
    H, W = img.shape[0], img.shape[1]
    # 기존에 3차원이었던 img 배열을 2차원 배열로 reshape
    new_img = img.reshape(H * W, 3)
    # 2차원 배열로 만든 new_img를 세로 열을 기준으로 (2, 2) 형태를 갖는 3개의 배열로 나눠주기
    RGB_arr = np.ravel(new_img, order='F').reshape(3, H, W)
    
    answer = np.zeros(shape = (len(img), len(img[0])))
    for i, w in zip(RGB_arr, [0.3, 0.5, 0.2]):
        answer += i * w

    return answer