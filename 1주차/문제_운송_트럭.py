# 운송 트럭

### 체감 난이도: 2
### dict 활용, 반복문와 조건문 활용

def solution(max_weight, specs, names):

    # 주어진 specs의 값을 상품을 key로, 누적 무게를 Value로 하는 dict 생성
    specs_dic = {item: size for item, size in specs}
    
    # 트럭의 수, 현재 트럭의 무게 변수 정의
    cnt, total = 1, 0
    
    for i in names:
        value = int(specs_dic[i])
        # 현재 트럭의 무게에 추가로 물건을 실어도 max_weight를 넘지 않는지 확인
        if total + value <= max_weight:
            total += value
        # 현재 트럭의 무게가 추가로 물건을 실어서 max_weight를 넘는 경우
        # 트럭의 수를 한 대 늘리고, 현재 트럭의 무게도 해당 아이템의 무게로 설정
        else:
            cnt += 1
            total = value
            
    return cnt