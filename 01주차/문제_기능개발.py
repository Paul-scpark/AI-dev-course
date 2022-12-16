# 기능 개발

### 체감 난이도: 3
### 반복문을 통한 리스트 인덱싱, zip 함수 활용

import numpy as np

def solution(progresses, speeds):
    
    # 올림을 통해서 현재 작업 진도와 속도에 따라 걸리는 날짜를 계산해서 day_lst에 append
    day_lst, answer_lst = [], []
    for p, s in zip(progresses, speeds):
        day_lst.append(np.ceil((100 - p) / s))
    
    ### [풀이 1] 조금 복잡한 로직...
    lst = []
    # day_lst 데이터에서 첫 인덱스가 다음 것보다 큰 것들을 계속 tracking 하는 로직 만들기
    for i in day_lst:
        # 가장 첫 데이터에는 lst가 비어 있으므로 현재 값을 추가
        if len(lst) == 0: lst.append(i)
        # 데이터가 하나라도 존재하는 lst의 경우에는 다음 값이 처음 값보다 큰 값인지 비교
        else: 
            # 가장 첫 값이 크다면, 계속해서 현재 값인 i를 append
            # 그렇지 않은 경우에는 최종적으로 lst의 길이를 answer_lst에 append 해주고, 다음 반복문 실행
            if lst[0] >= i: lst.append(i)
            else:
                answer_lst.append(len(lst))
                lst = [i]
    
    # 현재의 lst의 길이가 0이 아니면, lst에 값이 존재하므로 [len(lst)] 조건을 추가
    if len(lst) != 0:
        return answer_lst + [len(lst)]
    return answer_lst

    # ### [풀이 2] 로직을 조금 단순화 시키기
    # idx = 0
    # for i in range(len(day_lst)):
    #     if day_lst[idx] < day_lst[i]:
    #         answer_lst.append(i - idx)
    #         idx = i
    
    # answer_lst.append(len(day_lst) - idx)
    
    # return answer_lst