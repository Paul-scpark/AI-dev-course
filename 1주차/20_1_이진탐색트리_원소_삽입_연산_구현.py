# 20강 실습: 이진탐색트리의 원소 삽입 연산 구현

### 체감 난이도: 2
### 이진탐색트리 활용 및 구현

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if self.key is key:
            return False
            
        # Node 기준 key의 왼쪽과 오른쪽 확인
        if key < self.key:
            if self.left:
                self.left.insert(key,data)
            else:
                self.left = Node(key,data)
                
        elif key > self.key:
            if self.right:
                self.right.insert(key,data)
            else:
                self.right = Node(key,data)


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0