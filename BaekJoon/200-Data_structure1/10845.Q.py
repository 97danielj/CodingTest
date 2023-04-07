# 명령의 종류
# Q의 특징 : FIFO
# push X : 정수 X를 큐에 넣는 연산이다.
# pop : 큐에 가장 앞에 정수를 빼고, 그 수를 출력한다. len(Q) == -1
# size : 큐에 들어있는 정수의 개수를 출력한다.
#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력 : 첫째 줄에 주어지는 명령의 수 N
# 출력 : 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.


Q = []
def push(x, Q=Q):
    Q.append(x)

def pop(Q=Q):
    if empty() == 1:
        return -1
    else:
        pop_object = Q.pop(0)
        return pop_object
def size(Q=Q):
    return len(Q)

def empty(Q=Q):
    if len(Q) == 0:
       return 1
    else:
        return 0

def front(Q=Q):
    if empty() == 1:
        return -1
    return Q[0]

def back(Q=Q):
    if empty() == 1:
        return -1
    return Q[-1]


import sys
N = int(sys.stdin.readline())
for i in range(N):
    comm = sys.stdin.readline().split()
    if comm[0] == 'push':
        push(int(comm[1]))
    elif comm[0] == 'empty':
        print(empty())

    elif comm[0] == 'size':
        print(size())
    elif comm[0] == 'pop':
        print(pop())

    elif comm[0] == 'front':
        print(front())

    elif comm[0] == 'back':
        print(back())



