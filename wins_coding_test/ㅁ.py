def solution(grids):
    answer = []

    for grid in grids:
        # 왼쪽 상단과 오른쪽 하단 모서리의 픽셀을 찾음
        top_left = None
        bottom_right = None
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "X":
                    if top_left is None:
                        top_left = (i, j)
                    bottom_right = (i, j)

        # 검은색 직사각형의 개수가 1개인지 확인
        num_rectangles = 0
        for i in range(top_left[0], bottom_right[0]+1):
            for j in range(top_left[1], bottom_right[1]+1):
                if grid[i][j] != "X":
                    answer.append(False)
                    num_rectangles = 2
                    break
            if num_rectangles == 2:
                break
        if num_rectangles != 2:
            answer.append(True)

    return answer


print(solution([[".....", ".XXX.", ".X.X.", ".XXX.", "....."]]))