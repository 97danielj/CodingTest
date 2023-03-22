def solver(X):
    n = 1
    dir = False

    while True:
        X -= n # n개의 블록을 간다.
        dir = not dir  # 방향을 바꾼다.

        n += 1
        if X <= n: #다음 n개의 블록을 갈수 있나?
            break #못가면 break




    if X == 0: # 더 갈 필요가 없다.
        if dir == True:
            return 1, n-1
        else:
            return n-1, 1
    else:
        if dir == True:
            nemer = 1
            denom = n
            for i in range(X-1):
                nemer += 1
                denom -= 1
        else:
            nemer = n
            denom = 1
            for i in range(X-1):
                nemer -= 1
                denom += 1

    return nemer, denom


# 배열이 이루는 규칙 i,j => i/j 값을 가진다.
# 지그재그가 움직이는 수식
# n=1, 1개
# n=2, 2개 , i: 1~2, j : 1~2
# n=3, 3개, i: 1~3개, j : 1~3개
# n=4, 4개, i: 1~4개, j : 1~4개

X = int(input())
nemer, denom = solver(X)
print(f'{nemer}/{denom}')