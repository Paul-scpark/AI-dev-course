# 12강 실습: 중위표현 수식 -> 후위표현 수식

### 체감 난이도: 2
### Stack 활용 및 구현

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for i in S:
        # 알파벳인 경우에는 answer에 추가
        if i.isalpha(): answer += i
        # 괄호가 시작된 경우에는 스택에 push
        elif i == '(': opStack.push(i)
        # 괄호가 닫힌 경우에는 스택에 있는 항목들 pop
        elif i == ')':
            while not opStack.isEmpty():
                stack = opStack.pop()
                if stack == '(': break
                else: answer += stack
        
        # 알파벳이거나, 괄호가 아닌 경우에는 연산자의 우선 순위 확인
        else:
            while not opStack.isEmpty():
                if prec[opStack.peek()] >= prec[i]:
                    answer += opStack.pop()
                else: break
            opStack.push(i)
                
    while not opStack.isEmpty(): answer += opStack.pop()
                    
    
    return answer