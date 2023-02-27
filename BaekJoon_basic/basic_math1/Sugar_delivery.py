# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


def solver(N):
    five_kg = N // 5
    rest = N % 5
    if rest == 0:
        return five_kg
    else:
        three_kg = rest // 3
        if rest % 3 == 0:
            return five_kg + three_kg
        else:
            three_kg = N // 3
            rest = N % 3
            if rest ==0:
                return three_kg
            else:
                return -1




N = int(input())

print(solver(N))

