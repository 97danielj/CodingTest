#1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#3. 판매는 얼마든지 할 수 있다.


#알고리즘
# 오름차순으로 올라가다 최고점일때 팔면 최대 이익 실현
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input()) #예지 날짜 기간
    sale_price_list = input().split()
    sale_price_list = list(map(int,sale_price_list))

    #tmp = sale_price_list[0]
    sale_day = []
    day = None
    last_sale_price = 0
    current_sale_price = 0
    for i in range(n): #매매가 리스트 탐색, 현재 매매가가 이전 매매가 보다 크면 된다.
        if i == 0:
            current_sale_price = sale_price_list[0]
            continue
        last_sale_price = current_sale_price
        current_sale_price = sale_price_list[i]
        if current_sale_price >= last_sale_price:
            day = i #최고점을 계속 갱신
        else: # 꺽이는 시점이다.
            sale_day.append(day)

        # 마지막 시점에서의 비교
        if i == n-1:
            if current_sale_price > last_sale_price:
                sale_day.append(i)





    print(f'#{test_case}', end=' ')
    print(sale_day)


