# 카펫

### 체감 난이도: 3
### 약수 구하기, 수학적 사고 (방정식 만들기)

def solution(brown, red):
    
    # 카펫을 구성하고 있는 brown과 red가 있을 때, 이 상태를 수식으로 표현해보면 다음과 같음
    # brown = 2 * (width + height) - 4, red = (width - 2) * (height - 2)
    # [조건 1] width * height = brown + red
    # [조건 2] width + height = (brown + 4) / 2
    # 다음과 같이 brown과 red 값에 대하여 width와 height에 대한 수식으로 정의 가능
    
    divisor_lst = []
    for i in range(1, brown + red + 1):
        # [조건 1] width * height = brown + red 이므로, width와 height는 brown + red의 약수
        if (brown + red) % i == 0:
            # 주어진 i에 대해 (brown + red) 값을 만들 수 있는 각 약수의 값을 width와 height로 정의
            width, height = (brown + red) / i, i
            # [조건 2] width + height = (brown + 4) / 2이므로, 이 조건을 만족하는 width와 height 리턴
            if width + height == (brown + 4) / 2:
                return [width, height]