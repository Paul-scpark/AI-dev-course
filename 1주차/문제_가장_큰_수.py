# 최솟값 만들기

### 체감 난이도: 3
### map과 lambda 함수 활용

def solution(numbers):
    
    # list의 각 element가 int 타입인 것을 str 타입으로 변환하기 위해 map 함수 활용
    n = list(map(str, numbers))
    
    # [3, 30, 34, 5, 9] 값을 사전 순으로만 정렬하면, [9, 5, 34, 30, 3]와 같은 형태로 최댓값을 만들 수 없음
    # numbers의 원소는 1000 이하의 값이므로, 길이의 최댓값을 생각해서 3을 곱해주기 위해 lambda x: x * 3 식 작성
    # 따라서 [3, 30, 34, 5, 9]의 경우일 때, [999, 555, 343434, 303030, 333] 같이 출력
    # 이를 사전 순으로 정렬하게 되면, [999, 555, 343434, 333, 303030]으로 반환되므로 최댓값을 만들 수 있음
    return str(int(''.join(sorted(n, key = lambda x: x * 3, reverse = True))))