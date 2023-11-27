# brute-force: 난폭한 힘
# 모든 경우를 다 검사하여 원하는 값을 탐색
# 장점: 이론적 가능한 수 모두 탐색
# 단점: 수행하는데 자원의 소비가 많고, 오래 걸린다.

# 1. 배열 탐색
def findIndex(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. 문자열 비교
def stringCompare(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

    small_length = min(length_s1, length_s2)

    for i in range(small_length):
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])

    if (length_s1 == length_s2):
        return 0
    elif length_s1 > length_s2:
        return s1[small_length]
    else:
        return s2[small_length]