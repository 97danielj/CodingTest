tc = int(input())

directions = [[-1,-1], [0, -1], [1, -1]]
for i in range(tc):
    #금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    #다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    for col in range(1, m): # m-1번의 이동
        for row in range(n): #n개의 행
            loc = dp[row][col]
            for d in directions: # 3개의 방향
                if 0 <= row+d[0] <= (n-1) and 0 <= col+d[1] <= (m-1): #테이블 안에 존재 시에만
                    dp[row][col] = max(dp[row][col], loc + dp[row+d[0]][col+d[1]])
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)






