# 일단 나눠 지는 것이 중요하다
# 우선순위 : 5로 나나눠
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


def solver(sugar):
    bag = 0
    while sugar >= 0:
        if sugar % 5 == 0: #5의 배수이면
            bag += (sugar // 5)
            return bag

        sugar -= 3
        bag += 1

    else:
        return -1




sugar = int(input())

print(solver(sugar))

