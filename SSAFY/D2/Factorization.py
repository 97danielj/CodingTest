# N은 2, 3, 5, 7, 11로 이루어진 수


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
prime_list = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    prime_count = [0] * 5
    N = int(input())
    for i in range(5):
        while True:
            rest = N % prime_list[i] #나머지는지를 확인
            if rest != 0: #안 나눠 지면 break
                break
            N = N // prime_list[i]
            prime_count[i] += 1

    print('#{}'.format(test_case), *prime_count)


