# 더 맵게

### 체감 난이도: 2
### heap 활용

import heapq

def solution(scoville, k):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
    return answer