# 22강 실습: 최대 힙에 새로운 원소 삽입

### 체감 난이도: 2
### 이진탐색트리 활용 및 구현

class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        m = len(self.data) - 1
        
        while m > 1:
            # 부모 노드의 값보다 item이 더 클 경우 바꿔주기
            if self.data[m] > self.data[(m // 2)] :
                self.data[m], self.data[(m // 2)] = self.data[(m // 2)], self.data[m]
                m = m // 2 # index 조정
            else:
                break


def solution(x):
    return 0