# 행렬 덧셈
N, M = input().split()
N = int(N)
M = int(M)

A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]


for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j] +B[i][j], end=' ')
    if i != len(A)-1:
        print()