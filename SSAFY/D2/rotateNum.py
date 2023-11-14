def rotate90(arr):
    n = len(arr)
    init = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            init[i][j] = arr[n-1-j][i]
    return init


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N): #NxN 행렬 입력 받기
        row = input().split()
        arr.append(row)
    # 알고리즘
    # 모든것은 재귀
    # 테두리만 90도로 돌리는 것을 재귀함수로 생성
    # 1. 90도 돌리기
    #  5를 기준으로
    # 방향키 는 90도
    rt90 = rotate90(arr)
    rt180 = rotate90(rt90)
    rt270 = rotate90(rt180)

    print(f'#{test_case}')
    for i in range(N):
        print(''.join(rt90[i]), ''.join(rt180[i]), ''.join(rt270[i]))

