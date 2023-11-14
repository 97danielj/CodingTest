T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tmp = input().split()
    tmp = list(map(int, tmp))
    A = input().split()
    A = list(map(int, A))
    B = input().split()
    B = list(map(int, B))
    if len(A) <= len(B):
        small_target = A
        big_target = B
    else: small_target = B, big_target=A

    print(A)
    print(B)
    move = len(big_target) - len(small_target)

    # 테스트 케이스의 출력값
    sum_max = 0


    for trans in range(move+1): # 주어진 두 시퀀스에 대한 모든 연산
        # 서로 마주보는 숫자들을 곱한 뒤 더하는 연산
        tmp = 0
        for i in range(len(small_target)-1):
            tmp += small_target[i] * big_target[i+trans]
            print(tmp)
        if tmp > sum_max:
            sum_max = tmp

    print(f'#{test_case}', sum_max)


