T = int(input())


def reseller(N):
    sale_price = input().split()
    sale_price = list(map(int, sale_price))

    profit_list = [0 for i in range(N)]

    i = N - 1
    profit = 0
    while i > -1:
        j = i - 1

        current_price = sale_price[i]

        while j > -1:
            previous_price = sale_price[j]
            if current_price > previous_price:
                profit += (current_price - previous_price)  # 더한다.
                profit_list[j] = profit  # 옮긴다.
                j = j - 1
            else:
                break

        profit_list[j] = profit  # 옮기는 것
        i = j

    return profit_list[0]

for test_case in range(1, T+1):
    N = int(input())
    print("#{} {}".format(test_case, reseller(N)))




