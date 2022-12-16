# 2강 실습: (1) 리스트에 새로운 요소 삽입하기

### 체감 난이도: 1
### list의 활용 (index, sorted)

# 풀이 1
def solution(L, x):

    L.append(x)
    return sorted(L)

# 풀이 2
def solution(L, x):
    
    flag = True
    # 원소를 하나씩 보면서, 처음으로 x보다 큰 원소가 등장하는 경우
    # 그때의 index 값에 x를 insert 해주고, for문 반복 멈추기
    for i in range(len(L)):
        if x <= L[i]:
            L.insert(i, x)
            flag = False
            break
    
    # 끝까지 돌았는데, insert 하지 못한 경우는 주어진 x가 가장 큰 경우
    # 따라서 가장 마지막에 x를 append 해주기
    if flag: L.append(x)
    
    return L