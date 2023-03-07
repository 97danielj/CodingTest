# 시간 초과 방지를 위한 빠른 알고리즘 설계

# 1. 소수 확인 함수

# why? sqrt(n)까지만 확인?
# 1. 우선 n이 sqrt(n) 이하의 수로 나누어 떨어지지 않는다고 가정을 한다.
# 2. n = x * y라고 가정을 한다. 그러면 가정 1에 의해 x>sqrt(n) , y>sqrt(y)
# x*y >= y 이므로 명제 , 즉 어떤 수를 2개로 나눈다면  x, y중 하나는 sqrt(n)같거나 작다
def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
