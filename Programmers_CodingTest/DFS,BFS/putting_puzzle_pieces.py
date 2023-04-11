# 퍼즐 조각 채우기

# 1. 모형 어떻게 체크 -> 1이나 0인 부분 bfs 또는 dfs 로 탐색 좌표리스트를 묶음으로서 => graph 생성
# 2. 90도 회전 -> 90도 돌려서 3번 체크
# 3. 좌표만 보고 같은 모형인지 어떻게 체크 ? 해당 좌표들을 오름차순으로 정렬하고 시작값을 0, 0을 기능으로 상대좌표로 표시

# python
from collections import deque

d = [[-1,0],[0,1],[1,0],[0,-1]] #방향을 나타낸다.

def spin(block): # 배열을 90도 시계방향으로 회전시키는 기능을 먼저 구현
    spin_block = [[0]*len(block) for _ in range(len(block[0]))] #행과 열을 잘 판단
    for row in range(len(block)):
        for col in range(len(block[0])):
            spin_block[col][len(spin_block[0])-1-row] = block[row][col]
    return spin_block

# 인덱스에서 퍼즐 조각을 획득
def catch_piece(table,row,col):
    '''

    :param table: 퍼즐의 조각 상태
    :param row: 테이블에서 발견된 조각 놓인 칸의 행 인덱스
    :param col: 테이블에서 발견된 조각 놓인 칸의 열 인덱스
    :return : 현재 주어진 인덱스에서 발견한 퍼즐 행렬
    '''
    R,C = len(table),len(table)
    piece = [[0]*C for _ in range(R)] # 테이블과 같은 크기 2차원 배열

    # BFS로 조각 찾기
    q = deque([[row,col]]) #해당 인덱스 큐에 넣기
    piece[row][col] = 1 #방문(발견처리)
    table[row][col] = 0
    while q:
        r,c = q.popleft()
        for i in d:
            dr,dc = i # 현재의 방향
            if 0 <= r+dr < R and 0 <= c+dc < C: #현재 찾은 테이블 보드의 채워진 칸의 인덱스가 최소와 최대를 넘지 않는다면
                if table[r+dr][c+dc] == 1: # 현재 방향으로 다음 위치의 칸이 블록 칸이라면
                    table[r + dr][c + dc] = 0
                    piece[r + dr][c + dc] = 1
                    q.append([r+dr,c+dc])


    # 모든 열 0인 행은 삭제
    r_piece = []
    for i in piece:
        if sum(i) != 0: #그대로
            r_piece.append(i)

    r_piece = spin(r_piece) # 90도 회전
    c_piece = []
    for i in r_piece:
        if sum(i) != 0:
            c_piece.append(i) #그대로

    for _ in range(3):
        c_piece = spin(c_piece)
    return c_piece

def compare(game_board,piece,row,col):
    R,C = len(game_board),len(game_board)
    cnt = 0
    for r in range(len(piece)):
        for c in range(len(piece[0])):
            if piece[r][c] == 1 and game_board[row+r][col+c] == 2:
                cnt += 1
            elif piece[r][c] == 0 and game_board[row+r][col+c] == 1:
                continue
            else:
                return 0 #사이즈도 맞고, 얼 추 맞다가 추후에 안맏다 ex) piece - 1
    return cnt


def solution(game_board,table):
    answer = 0
    piece = deque() # 조각을 위한 deque
    R,C = len(game_board),len(game_board)
    for row in range(R):
        for col in range(C):
            if table[row][col] == 1: #테이블에 조각 놓인 칸이라면
                piece.append(catch_piece(table,row,col)) #그 위치에 조각을 획득해보자
                # 조각들 모음

    print(piece)
    for row in range(R):
        for col in range(C):
            if game_board[row][col] == 0:
                q = deque([[row,col]])
                min_row,max_row = row,row
                min_col,max_col = col,col
                while q:
                    r,c = q.popleft()
                    game_board[r][c] = 2
                    for i in d:
                        dr,dc = i
                        if 0 <= r+dr < R and 0 <= c+dc < C:
                            if game_board[r+dr][c+dc] == 0:
                                q.append([r+dr,c+dc])
                                min_row,max_row = min(min_row,r+dr),max(max_row,r+dr)
                                min_col,max_col = min(min_col,c+dc),max(max_col,c+dc)
                                game_board[r+dr][c+dc] = 2

                result = 0 #현재 조각으로 채울 수 있는 칸수
                for p in range(len(piece)):
                    for _ in range(3): # 4번까지 돌리면 된다.
                        if piece[p][0][0] == -1:  # 조각 중복 금지
                            break
                        if len(piece[p]) == max_row-min_row+1 and len(piece[p][0]) == max_col-min_col+1:
                            result = compare(game_board,piece[p],min_row,min_col)
                            if result > 0: # 딱 맞아 떨어 졌다.
                                answer += result #최종 대답에 result를 합해준다.
                                piece[p][0][0] = -1
                                break
                        piece[p] = spin(piece[p]) # 안맞아 떨어진 경우
                    if result > 0: #이건 왜 필요한가? => 현재 game_board 인덱스에 딱맞는 조각 찾았으니 다른 조각 비교할 필요 없다.
                        break

    print(game_board)
    return answer
