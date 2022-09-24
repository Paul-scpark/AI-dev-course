# 4강 실습: 피보나치 순열

### 체감 난이도: 1
### 재귀 함수의 활용

def solution(x):
    
    # 종결 조건 - x가 0이거나 1인 경우
    if x == 0: return 0
    elif x == 1: return 1
    # 반복 조건 - x가 1보다 큰 경우에는 반복적으로 재귀 함수를 호출
    else: return solution(x - 1) + solution(x - 2)