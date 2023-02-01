# 입력 조건
'''
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w
'''


# 격자판 크기
w, h = input().split()
w = int(w); h = int(h)

#격자 생성
matrix = [[0 for j in range(h)] for i in range(w)]

# 막대의 개수
n = int(input())

# 각 막대의 위치를 격자판에 표현

for test_case in range(n):
     l, d, x, y = list(map(int, input().split()))
     x -= 1
     y -= 1
     for size in range(l):
         #가로방향 배치
         if d == 0:
            matrix[x][y+size] = 1
         else:
             matrix[x+size][y] = 1


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()