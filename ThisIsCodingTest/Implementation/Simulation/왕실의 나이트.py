# 입력 : 나이트 행렬에서 위치
# 출력 : 나이트 이동가능한 경우의 수



# 수직으로 움직일 때
dx1 = [[-1, -1],[1,1]]
dy1 = [-1,1]

# 수평으로 움직일 때
dx2 = [-1,1]
dy2 = [[-1,-1], [1, 1]]

# TIP) 나이트가 이동할 수 있는 8가지 방향 정의 하면 된다.
steps = [(-2,-1), (-2, 1), (2,  -1), (2, 1), (-1,2), (1, 2), (-1,-2), (-1, -2)]
def solver(location):
    c_row = int(location[1]) - 1
    c_col = int(ord(location[0]) - 97)

    count = 0
    dir = 0
    # 수직으로 움직일 때 count
    for i in dx1:
        tmp_row = c_row
        for k in i:
            tmp_row += k
            if tmp_row < 0 or tmp_row > 7:
                break
            # row 방향(수직)으로 움직였을 때 만족한다면
        else:
            for j in dy1:
                tmp_col = c_col
                tmp_col += j
                if tmp_col >= 0 and tmp_col <= 7:
                    count += 1



    for j in dy2:
        tmp_row = c_row
        for k in j:
            tmp_col += k
            if tmp_col < 0 or tmp_col > 7:
                break
        else:
            for i in dx2:
                tmp_row = c_row
                tmp_row += i
                if tmp_row >= 0 and tmp_row <= 7:
                    count +=1

    return count



location = input()
print(solver(location))
