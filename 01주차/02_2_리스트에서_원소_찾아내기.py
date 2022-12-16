# 2강 실습: (2) 리스트에서 원소 찾아내기

### 체감 난이도: 1
### list의 활용 (index), for문에서의 enumerate 함수 활용

# 풀이 1
def solution(L, x):
    
    answer = []
    # for 문에서 enumerate 함수를 통해 idx와 value 데이터를 확인
    # value가 x와 일치하는게 있다면, 그 idx를 answer 리스트에 append
    for idx, value in enumerate(L):
        if value == x:
            answer.append(idx)
    
    # answer 리스트에 원소가 하나도 없는 경우에는 주어진 조건에 따라 [-1] return
    if len(answer) == 0:
        return [-1]
    return answer

# 풀이 2
def solution(L, x):
    answer = []
    while True:
        # L 리스트 내에 x라는 요소가 있는지 index 함수로 확인
        # 혹시 있다면, index 값을 answer 리스트에 추가
        # 그리고 뒤에 추가적으로 x 값이 나올 수도 있으므로, 전에 나왔던 값은 0이라는 임의의 값으로 수정
        try:
            answer.append(L.index(x))
            L[L.index(x)] = 0
        # answer 리스트 내에 원소가 하나도 없으면 [-1] return
        # 하나라도 있다면, 해당 answer 리스트를 return
        except:
            if len(answer) != 0:
                return answer
            return [-1]