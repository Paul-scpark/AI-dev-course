# 나머지 한 점

### 체감 난이도: 1
### dict 활용

# target 값을 key로 하고, 반복되서 존재하는 횟수를 value로 하는 dic 생성
def making_dic(dic, target):
    if target in dic.keys(): dic[target] += 1
    else: dic[target] = 1
    
    return dic

def solution(v):
    
    x_dic, y_dic = {}, {}
    for x, y in v:
        x_dic = making_dic(x_dic, x)
        y_dic = making_dic(y_dic, y)
    
    # 위에서 만든 x와 y에 대한 dic에서 value 값이 1개인 값이 남은 한 점 값
    return [i for i in x_dic if x_dic[i] == 1] + [i for i in y_dic if y_dic[i] == 1]