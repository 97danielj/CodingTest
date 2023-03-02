# 행렬 덧셈
M, N = input().split()
M = int(M)
N = int(N)

A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]


for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j] +B[i][j], end=' ')
    if i != len(A)-1:
        print()
