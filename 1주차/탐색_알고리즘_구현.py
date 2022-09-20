
# 선형 탐색 알고리즘
def linear_search(L, x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1

    if i < len(L): return i
    else: return -1

# 이진 탐색 알고리즘
def binary_search(L, x):
    idx = -1
    lower, upper = 0, len(L) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x: return middle
        elif L[middle] < x: lower = middle + 1
        else: upper = middle - 1