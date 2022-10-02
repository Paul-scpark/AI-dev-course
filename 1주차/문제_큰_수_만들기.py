# 큰 수 만들기 문제

### 체감 난이도: 3
### Greedy의 활용, 효율적 반복문의 사용

def solution(number, k):
    collected = []
    
    for idx, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[idx:])
            break
        collected.append(num)
    
    collected = collected[:-k] if k > 0 else collected
    
    return ''.join(collected)