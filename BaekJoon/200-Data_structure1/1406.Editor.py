# Editor
# 목적 : 편집기 구현
# L : 왼쪽 한칸
# R : 오른쪽 한칸
# B : 커서 왼쪽에 있는 문자를 삭제.
# P $ : $라는 문자 왼쪽에 추가

import sys
text = sys.stdin.readline()
text = text[:-1]
comm_N = int(sys.stdin.readline())

def L(cursor_idx):
    if cursor_idx != 0:
        cursor_idx -= 1
    return cursor_idx

def D(cursor_idx):
    if cursor_idx != len(text):
        cursor_idx += 1
    return cursor_idx

def B(cursor_idx, text):
    if cursor_idx != 0:
        text = text[:cursor_idx-1] + text[cursor_idx:]
        cursor_idx -= 1
    return text, cursor_idx

def P(cursor_idx , text, char):
    text = text[:cursor_idx] + char + text[cursor_idx:]
    cursor_idx += 1
    return text, cursor_idx


cursor_idx = len(text)
for i in range(comm_N):
    comm = sys.stdin.readline().split()
    if comm[0] == 'P':
        text, cursor_idx = P(cursor_idx, text, comm[1])
    elif comm[0] == 'L':
        cursor_idx = L(cursor_idx)
    elif comm[0] == 'D':
        cursor_idx = D(cursor_idx)
    elif comm[0] == 'B':
        text, cursor_idx = B(cursor_idx, text)

print(text)



