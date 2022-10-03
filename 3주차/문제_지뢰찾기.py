# 지뢰찾기 문제

### 체감 난이도: 2
### numpy - where 함수 활용, split 함수 활용

import numpy as np

def solution(board, bombs):
    
    idx = 0
    # 가장 먼저는 가로 (행) 단위로 주어진 board 배열을 split
    for i in np.split(board, 2):
        # 그 후에 행 단위로 split 된 배열을 열 단위로 다시 한번 split
        # 이렇게 하면 최종적으로 board[0:5, 0:5], board[0:5, 5:10], board[5:10, 0:5], board[5:10, 5:10]으로 나뉨
        # 그 상태에서 bombs에 주어진 항목과 일치하는 자리에 요소를 0으로 수정
        for j in np.split(i, 2, axis = 1):
            j[np.where(j == bombs[idx])] = 0
            idx += 1
            
    return board