
import sys
now = 1
stack_list = list()
operation_list = list()

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())

    while now <= num:
        stack_list.append(now)
        operation_list.append('+')
        now += 1

    if stack_list.pop() != num:
        print("NO")
        break

    operation_list.append("-")

else:
    for i in operation_list:
        print(i)

