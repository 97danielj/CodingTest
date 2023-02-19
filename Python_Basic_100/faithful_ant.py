# 미로 입력 받기

matrix = [list(map(int,input().split())) for i in range(10)]

current_position = [1, 1]

# 먹이 탐색 시작

matrix[current_position[0]][current_position[1]] = 9

while True:
    # 행우선 탐색
    if matrix[current_position[0]][current_position[1]+1] != 1:
        target = matrix[current_position[0]][current_position[1]+1]
        current_position[1] = current_position[1] + 1
        matrix[current_position[0]][current_position[1]] = 9
        if target == 2:
            break
    # 열 우선 탐색
    elif matrix[current_position[0] + 1][current_position[1]] != 1:
        target = matrix[current_position[0] + 1][current_position[1]]
        current_position[0] = current_position[0] + 1
        matrix[current_position[0]][current_position[1]] = 9

        if target == 2:
            break


    #더이상 아래로 움직일 수 없을 경우 or 먹이를 찾은 경우
    else:
        break

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()