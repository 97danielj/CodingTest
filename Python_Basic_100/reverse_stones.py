# 바둑판 배열을 입력받은다.

d = []
for i in range(19):
    row = list(map(int,input().split())) #행을 리스트로 받는다.
    d.append(row)

n = int(input())

for test_case in range(n):
    i , j = map(int,input().split())
    i = i-1
    j = j-1

    # 해당 위치 행을 reverse
    for c_index in range(19):

        target1 = d[i][c_index]

        if target1 == 0:
            d[i][c_index] = 1
        else:
            d[i][c_index] = 0

    # 해당 위치의 열을 reverse

    for r_index in range(19):
        target2 = d[r_index][j]

        if target2 == 0:
            d[r_index][j] = 1
        else:
            d[r_index][j] = 0


for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print()




