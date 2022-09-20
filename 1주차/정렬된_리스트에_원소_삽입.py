# 2강 실습: (1) 리스트에 새로운 요소 삽입하기

### 체감 난이도: 1
### list의 활용 (index, sorted)

def solution(L, x):

    L.append(x)
    return sorted(L)