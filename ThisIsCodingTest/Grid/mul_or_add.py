# 입력 : 문자열 S
# 요구사항 : 1. 왼쪽 부터 오른쪽 모든 숫자 확인 하며 연산자 넣어 만들어질 수 있는 가장 큰수를 구하는 프로그램
#           2. 단, 연산 우선순위는 이때 무시. 왼쪽 -> 오른쪽

# 아이디어 : 그리드 방식 -> x이 많을 수록 좋다. 단 0을 제외하고


def solution(s):


    s = list(map(int, list(s)))

    sum = s[0]
    for i in range(1, len(s)):
        num = s[i]
        if num > 1 and sum > 1:
            sum *= s[i]
        else:
            sum += s[i]

    return sum


print(solution("567"))
