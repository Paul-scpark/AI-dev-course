# 완주하지 못한 선수 문제

### 체감 난이도: 2
### 해쉬 활용, dictionary의 get 함수 활용

def solution(participant, completion):
        
    dic = {}
    # dic에 값이 있으면 += 1 하고, 없으면 1로 설정하도록 하는 get 함수
    for i in participant:
        dic[i] = dic.get(i, 0) + 1
    for i in completion:
        dic[i] -= 1
    
    # 주어진 dic의 value 값이 0보다 큰 key 값을 return 
    return [key for key in dic if dic[key] > 0][0]