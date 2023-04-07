## 스택을 2개 이용
# 서로의 값을 왔다 갔다 => L, D
# 추가 stack1 append
# 삭제 stack1 pop


import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []

for _ in range(int(sys.stdin.readline())):
    comm = sys.stdin.readline().split()
    if comm[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif comm[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif comm[0] == 'P':
        stack1.append(comm[1])
    elif comm[0] == 'B':
        if stack1:
            stack1.pop()

stack1.extend(reversed(stack2))
print(''.join(stack1))


