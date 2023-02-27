# 반상회
# 제한 : 1 ≤ k, n ≤ 14
def solver(k, n):
    matrix = [[0 for j in range(n+1)] for i in range(k+1)] # (k+1) X (n+1) 행렬 생성

    for floor in range(k+1):
        for room_number in range(n+1):
            if floor == 0:
                matrix[0][room_number] = room_number
            else:
                room_sum = 0
                for idx in range(room_number+1):
                    room_sum += matrix[floor-1][idx]
                matrix[floor][room_number] = room_sum

    return matrix[k][n]





T = int(input())

for test_case in range(T):
    k = int(input()) # 층 수
    n = int(input()) # 호 수
    print(solver(k, n))
