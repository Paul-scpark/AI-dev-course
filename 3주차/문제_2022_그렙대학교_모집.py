# 데이터 필터 문제

### 체감 난이도: 2
### numpy - isnan 함수 활용, numpy array의 인덱싱

import numpy as np

def solution(data):
    
    answer_lst = []
    for i in data:
        # nan인 항목들은 제거하기
        stu_lst = i[~np.isnan(i)]
        
        # 주어진 조건에 따라 학생 정보 중에서 0번과 1번 인덱스는 
        # 각각 학생의 이름, 학생의 지원 전형 그리고 그 외에는 점수가 담겨 있음
        stu = stu_lst[0]
        stu_type = stu_lst[1]
        stu_score = stu_lst[2:]
        
        # 지원 전형에 따른 학생의 점수 (score) 계산하여 통과 여부 확인
        if stu_type == 0:
            if (stu_score[0] * 0.3) + (stu_score[1] * 0.3) + (stu_score[2] * 0.4) >= 0.8:
                answer_lst.append(stu)
        elif stu_type == 1:
            if (stu_score[0] * 0.5) + ((stu_score[1] * 0.3) + (stu_score[2] * 0.4) + (stu_score[3] * 0.3)) * 0.5 >= 0.75:
                answer_lst.append(stu)
        elif stu_type == 2:
            if (stu_score[0] * 0.3) + (stu_score[1] * 0.4) + (stu_score[2] * 0.3) >= 0.75:
                answer_lst.append(stu)
    
    return sorted(answer_lst)