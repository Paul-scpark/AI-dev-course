# 예산 소팅 문제

### 체감 난이도: 1
### list의 정렬 (sorted), 반복문 활용

def solution(d, budget):
    
    answer, curr = 0, 0
    # 부서 별 예산이 담긴 d를 정렬
    for i in sorted(d):
        # 작은 순서대로 누적하면서 budget을 넘지 않는 범위까지의 부서 수 확인
        if curr + i <= budget:
            curr += i
            answer += 1
            
    return answer