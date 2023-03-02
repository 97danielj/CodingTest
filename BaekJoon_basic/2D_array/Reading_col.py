# long length 기준으로 배열을 만든다.

def solver(board):
    max_len = 0
    for i in range(5):
        if len(board[i]) > max_len:
            max_len = len(board[i])

    for j in range(max_len):
        for i in range(5):
            try:
                print(board[i][j], end='')
            except IndexError as e:
                pass



board = []
for i in range(5):
    board.append(input())


solver(board)


