# 3강 실습: 이진 탐색 구현하기

### 체감 난이도: 1
### 이진 탐색 알고리즘

def solution(L, x):
    
    idx = -1
    lower, upper = 0, len(L) - 1

    # lower와 upper 사이의 중간값인 middle로 index 위치 찾기
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x: return middle
        elif L[middle] < x: lower = middle + 1
        else: upper = middle - 1
        
    return -1