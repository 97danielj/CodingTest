# 괄호문자열이란?
# 입력 조건 : "(", ")" 으로만 구성, VPS를 만족
# VPS : 한쌍의 괄호를 만족해야 한다. "()"
# 입력 : 괄호 문자열
# 출력 : VPS인지 판단

# 카운트 만으로 될 일이 아니다.

import sys
def solver(ps_input: list):
    stack = []
    for char in ps_input:
        if char == "(":
            stack.append("(")
        elif char == ")":
            try:
                stack.pop()
            except:
                return "NO" #"("이 스택이 남지 않은 경우 바로 "NO"
    if len(stack) != 0: #쌍이 안맞아서 "("이 스택에 남은 경우
        return "NO"
    else:
        return "YES"



N = int(sys.stdin.readline())

for i in range(N):
    ps_input = sys.stdin.readline()
    print(solver(ps_input))



