def solver(n, k):

    count = 0

    t = 1
    while True:
        if t > n:
            return 0

        # count올리기
        if n % t == 0:
            count += 1

        # k카운트까지 왔다면 약수 t를 반환
        if count == k:
            return t

        t += 1


n, k = map(int, input().split())
print(solver(n, k))
