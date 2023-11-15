T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    operand = input().split()
    operand = list(map(int, operand))
    a,b = operand[0], operand[1]
    print(f'#{test_case}', end=' ')

    if a > b:
        print('>')
    elif a < b:
        print('<')
    else: print('=')

