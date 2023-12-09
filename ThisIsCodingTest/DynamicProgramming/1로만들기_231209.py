# 1. 문제 정의
# 정수 X가 주어졌을 때 4가지 연산을 진행할 수 있고
# 연산을 하여 최종적으로 값을 1로 만들고자 합니다.

# 2. 예시 파악
# Input: 26 / 26 -> 25 -> 5 -> 1 / Output: 3

# 3. 입력: X(1 <= X <= 30,000)
# 4. 출력: 첫째 줄에 연산을 하는 횟수의 최솟값을 출력

# 문제 해결 아이디어
# 시간 복잡도: (1 <= X <= 30,000) NLogN
# 최적해를 찾는다. : 1. 완전 탐색X, # 2. 파라매트릭 서치 X, #3. DP O

# dp 절차
# 1. dp조건 확인 / 최적 부분구조 O, 중복 부분문제 O
# 2. 변수 파악. dp[X] : 입력값 X를 1로 만들기 위한 연산 최소 횟수
x = int(input())

# 3. 관계식 정의
# ai는 i를 1로 만들기 위한 점화식
# 부분 문제 구조에서 점화식을 따온다.
# a_i = min(a(i-1), a(i/2), a(i/3), a(i.5)) + 1

# 4. 메모하기
dp = [0] * 30001

# 5. 기저 상태 파악
dp[0] = None
dp[1] = 0

# 6. dp 구현하기(bottom-up)

for i in range(2, x+1):
    # 현재 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    # 현재 수에서 2을 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    # 현재 수에서 3을 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 현재 수에서 5를 나누는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])

