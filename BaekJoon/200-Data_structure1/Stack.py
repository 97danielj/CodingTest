import sys
N = int(sys.stdin.readline()) #표준 입력에서 한 줄을 입력받는다.
stack_list = []



def push(k:int):
    stack_list.append(k)

def empty():
    if len(stack_list) == 0:
        return 1
    else:
        return 0

def pop():
    if empty() == 0:
        value = stack_list.pop()
        return value
    else: return -1


def size():
    return len(stack_list)


def top():
    if empty() == 1:
        return -1
    else:
        return stack_list[-1]


for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())
    elif command[0] == "size":
        print(size())
    elif command[0] == "pop":
        print(pop())






