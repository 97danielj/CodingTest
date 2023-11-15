
# 요구 조건 : N과 K가 주어 지면 N을 연산 2개를 활용하여 1로 만드시오

# 입력 : 첫째줄 N(1<N<=100,000)과 K(2 <= K <= 100,000) 가 공백을 기준으로 하여 각각 자연수로 주어진다.
# 대체로 O(nlogn)
# 출력 : 첫째 줄에 N이 1이 될 때 가지 1번 혹은 2번의 과정을 수행해야하는 횟수 최솟값을 출력


# grid => 2번 연산으로 가장 많은 시도


def solution(n, k):
    count = 0
    while n > 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1
    return count


print(solution(25,3))