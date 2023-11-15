

loc = input()


steps = [(2,1),(2,-1),(-1, -2), (1, -2), (-2, 1), (-2, -1), (1, 2), (-1,2)]
def solver(loc):
    row = int(loc[1]) - 1
    col = ord(loc[0]) - ord('a')

    count = 0
    for step in steps:
        tmp_row = row
        tmp_col = col
        tmp_row += step[0]
        tmp_col += step[1]
        if 0 <= tmp_row <=7 and 0 <= tmp_col <= 7:
            count+=1
    return count




print(solver(loc))







