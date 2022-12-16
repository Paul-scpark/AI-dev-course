# 5강 실습: 재귀적 이진탐색

### 체감 난이도: 1
### 재귀 함수의 활용

def solution(L, x, l, u):
    # 종결 조건
    if l > u: return -1
    # 이진탐색을 위해서 시작 점과 끝 점 사이의 값을 mid로 정의
    mid = (l + u) // 2
    if x == L[mid]: return mid
    elif x < L[mid]: return solution(L, x, l, mid - 1)
    else: return solution(L, x, mid + 1, u)