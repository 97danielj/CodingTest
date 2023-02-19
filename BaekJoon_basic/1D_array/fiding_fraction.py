def solver(X):
    n = 1
    dir = False

    while True:
        X -= n
        dir = not dir

        if X <= n:
            break
        n += 1



    if X == 0:
        if dir == True:
            return 1, n
        else:
            return n, 1
    else:
        if dir == True:
            nemer = 1
            denom = n+1
            for i in range(X-1):
                nemer += 1
                denom -= 1
        else:
            nemer = n+1
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