# 운송 트럭

### 체감 난이도: 2
### list의 정렬 (sorted), 반복문과 조건문 활용, 순열 및 조합 활용 (from itertools import combinations)

from itertools import combinations

def solution(m, weights):
    
    flag = True
    answer, choice = 0, 1
    while flag:
        # weights의 값을 작은 수부터, 큰 순서로 정렬한 상태로 로직 만들기
        # 1부터 계속 수를 1씩 증가시키는 Choice에 대하여 가능한 조합 (combinations) 생성
        for idx, value in enumerate( list(combinations(sorted(weights), choice)) ):
            # 만약 가장 첫 조합의 숫자 합이 m 보다 큰 경우에는 반복문 멈추기 (weights가 sorted 되어 있기 때문에 가능)
            if (idx == 0) and (sum(value) > m): flag = False
            if m == sum(value): answer += 1
        choice += 1
        
        # 만약 m이 너무 큰 숫자여서 모든 weights의 원소 합으로도 만족시키지 못한다면, 반복문 멈추기
        if choice > len(weights): break
    
    return answer