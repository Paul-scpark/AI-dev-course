# 7강 실습: 연결 리스트 순회

### 체감 난이도: 2
### Linked List 활용 및 구현

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    
    def traverse(self):
        result = []
        # 현재를 head로 두고, 마지막 tail의 값인 None이 나올 때까지 반복해서 data를 append
        temp = self.head
        while temp != None:
            result.append(temp.data)
            temp = temp.next
        
        return result

# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0