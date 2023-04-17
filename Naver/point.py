
# x는 충전 단위
# y는 구매후 마일리지 적립에 걸리는 날짜
point = 0
mileage = 0
total_charge = 0
total_withdraw = 0



def buy(x, price):
    global point
    global mileage
    global total_charge

    if mileage >= price:
        mileage -= price
    else:
        rest_price = price - mileage
        mileage = 0
        if point >= rest_price:
            point -= rest_price
        else:
            charge_count = rest_price // x + 1
            total_charge += (charge_count * x)
            point += total_charge #충전한 금액을 포인트에
            point -= rest_price


def making_withdraw(withdraw):
    global point
    global total_withdraw
    if withdraw <= point:
        point = point-withdraw
        total_withdraw += withdraw
    else:
        total_withdraw += point
        point = 0



def making_mileage(last_day_price):
    global mileage
    mileage += int(last_day_price*0.1)



def solver(x, y, history):
    last_buy_day = 0 # 최근 구매
    last_buy_price = 0 # 최근 구매 가격

    for comm in history:
        hist = comm.split()
        current_day = int(hist[0]) #최근 내역 날짜

        if int(hist[2]) > 0:
            buy(x, int(hist[2]))
            last_buy_price = int(hist[2]) #최근 구매 가격
            current_buy_day = int(hist[0]) #최근 거래 날짜

        elif int(hist[2]) < 0:
            making_withdraw(-int(hist[2]))

        if last_buy_day+y <= current_day and last_buy_day+y <= 30:
            making_mileage(last_buy_price)
            last_buy_day = current_buy_day #다음 차례 넣을 수 있다.


    return [total_charge, total_withdraw, point, mileage]

print(solver(10000,3,['12 12:00 23000', '16 23:00 12000']))

