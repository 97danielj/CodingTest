from collections import deque

deque_list = deque()

for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.rotate(2)
print(deque_list)

deque_list.rotate(2)
print(deque_list)

print(deque(reversed(deque_list)))