
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    N = int(input())
    total_distance = 0
    speed = 0
    for i in range(N):
        command = input().split()
        command = list(map(int, command))
    # 1. 새로운 속도를 구하고
    # 2. 토탈 디스턴스를 계산한다.
        select = command[0]
        if select == 0:
            total_distance+=speed
        elif select == 1:
            speed += command[1]
            total_distance += speed
        elif select ==2:
            speed -= command[1]
            if speed <0:
                speed =0
            total_distance += speed
    print('#{}'.format(test_case), total_distance)







    # ///////////////////////////////////////////////////////////////////////////////////
