# 8강 실습: 연결 리스트 노드 삭제

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

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return False

        if pos == 1:  
            curr = self.head
            self.head = curr.next
            if pos == self.nodeCount : self.tail = self.head  

        else:
            prev = self.getAt(pos - 1)
            curr = prev.next
            prev.next = curr.next

            if pos == self.nodeCount: self.tail = prev

        self.nodeCount -= 1
        result = curr.data
        del(curr)
        
        return result

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

def solution(x):
    return 0