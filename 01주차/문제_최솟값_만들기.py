# 최솟값 만들기

### 체감 난이도: 1
### list의 정렬 (sorted), 반복문에서 zip 함수 활용

def solution(A,B):
    
    # A와 B를 각각 작은 순서, 큰 순서대로 정렬
    A, B = sorted(A), sorted(B, reverse = True)
    
    answer = 0
    # (작은 수 * 큰 수)로 계산된 값을 누적해서 더한 것이 가장 최솟값이 될 것
    for a, b in zip(A, B): answer += (a * b)
        
    return answer