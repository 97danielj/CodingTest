
# 문제점 : n이 소수인지 판별하기 위해 n보다 작은 모든 수로 나누어 보는 판단은 무식하다.
#에라토스네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
# 1. 1을 제거
# 2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 지운다.
# 3. 지워지지 않은 수 중 제일 작은 3를 소수로 채택하고, 나머지 3의 배수를 지운다.
# 4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 지운다.
# 5. (반복)


# 파이썬 코드의 표현

'''n=1000
a = [False,False] + [True]*(n-1)
primes=[]



for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i): # i =2 일시 range(2, 1001, 2)
        a[j] = False
print(primes)'''

# 주어진 수 만큼 행렬 n을 생산한다.
# 인덱스 0과 1은 배제
# 제일 작은 2부터 그 배수들을 제거
# 제일 작은 3부터 그 배수들을 제거
# 4는 선택되지 않는데 이미 False를 가졌기 때문


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
print(prime_list(9))


def prime_list1(n):
    sieve = [True] * n


    for i in range(2, int(n ** 0.5)+1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
    return [i for i in range(2,n) if sieve[i] == True]


print(prime_list1(20))

