# 올바른 괄호 문제
# (이면 )으로 닫혀야 하낟.

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else : #문자열이 ')'
            if stack == []:
                return False
            else:
                stack.pop()

    if stack: # 존재하낟.
        return False
    else:
        return True


