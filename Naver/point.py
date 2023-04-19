
# x는 충전 단위
# y는 구매후 마일리지 적립에 걸리는 날짜
point = 0
mileage = 0
total_charge = 0
total_withdraw = 0

from collections import deque
buy_days_queue = deque()
buy_price_queue = deque()

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
            point += x*charge_count #충전한 금액을 포인트에
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



def solver(x, y, pays):
    global mileage
    for pay in pays:
        pay_list = pay.split()
        while len(buy_days_queue) > 0 and buy_days_queue[0] + y <= int(pay_list[0]) and buy_days_queue[0] + y <= 30:
            buy_days_queue.popleft()
            target_price = buy_price_queue.popleft()
            mileage += int(target_price*0.1)

        if int(pay_list[2]) > 0:
            last_buy_day = int(pay_list[0])
            last_buy_price = int(pay_list[2])
            buy(x, last_buy_price)
            buy_days_queue.append(last_buy_day)
            buy_price_queue.append(last_buy_price)

        elif int(pay_list[2]) < 0:
            making_withdraw(-int(pay_list[2]))
    else :
        while len(buy_days_queue) > 0 and buy_days_queue[0] + y <= 30:
            buy_days_queue.popleft()
            target_price = buy_price_queue.popleft()
            mileage += int(target_price*0.1)

    return [total_charge, total_withdraw, point, mileage]

print('총충전금액, 총출금금액, 남은 포인트, 남은 마일리지')
print(solver(10000,3,['12 12:00 23000', '16 23:00 12000', '16 21:00 8000', '28 21:00 10000' ]))

