# 체육복 문제

### 체감 난이도: 2
### Greedy, 해쉬 활용, set 함수 활용

def solution(n, lost, reserve):
    
    # set 함수를 통해 교집합 및 차집합 원소 확인
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s

    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
        
    return n - len(l)