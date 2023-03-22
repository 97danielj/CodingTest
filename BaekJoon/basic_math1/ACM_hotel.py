# 전제조건 만약 1~6 이다 .그럼
def solver(H, W, N):

    num = N // H +1 # N 엘리베이터부터 거리, 호텔의 열 col
    floor = N % H # 호텔의 층, row

    if floor == 0:
        num = N // H
        floor = H

    num = str(num)
    if len(num) == 1:
        num = '0' + num

    room_assign = str(floor)+num
    return room_assign

T = int(input())

for test_case in range(T):
    H, W, N = map(int, input().split())
    print(solver(H, W, N))