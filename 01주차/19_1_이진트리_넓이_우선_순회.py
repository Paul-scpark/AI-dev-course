# 19강 실습: 이진트리의 넓이 우선 순회

### 체감 난이도: 2
### 이진트리 활용 및 구현

class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        # 빈 리스트, 빈 큐 초기화
        traversal, visitQueue = [], ArrayQueue()

        # 빈 트리가 아니면 루트 노드가 있으므로, 큐에 루트 노드를 인큐
        if self.root:
            visitQueue.enqueue(self.root)

        # 큐가 비어 있지 않는 동안 반복
        while visitQueue.isEmpty() == False:
            node = visitQueue.dequeue()
            traversal.append(node.data)

            # 노드에 왼쪽 or 오른쪽 자식 노드가 존재하는 경우 큐에 저장
            if node.left:
                visitQueue.enqueue(node.left)
            if node.right:
                visitQueue.enqueue(node.right)
            
        return traversal


def solution(x):
    return 0