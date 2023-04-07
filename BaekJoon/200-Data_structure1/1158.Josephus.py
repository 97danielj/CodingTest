# 조건 : 요세푸스. 제거되는 순으로 시계 순으로 K 번째

# 입력 : N과 K

# 출력 : 요세푸스 순열 리턴
def solver(n, k):
    seats = [i for i in range(1, n+1)]
    jose_seq = []
    head = -1 #idx

    while seats:
        if head+k <= len(seats) - 1:
            head = head+k
            jose_seq.append(seats.pop(head))
            head -=1
        else:
            head = ((head+k) % len(seats))
            jose_seq.append(seats.pop(head))
            head -=1

    print("<", end='')
    for i in range(len(jose_seq)-1):
        print(f'{jose_seq[i]}, ',end='')
    else:
        print(jose_seq[-1], end='')
        print(">", end='')


import sys
n, k = map(int,sys.stdin.readline().split())
solver(n, k)


