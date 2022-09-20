# 2강 실습: (2) 리스트에서 원소 찾아내기

### 체감 난이도: 1
### list의 활용 (index), for문에서의 enumerate 함수 활용

def solution(L, x):
    
    answer = []
    for idx, value in enumerate(L):
        if value == x:
            answer.append(idx)
    
    if len(answer) == 0:
        return [-1]
    return answer