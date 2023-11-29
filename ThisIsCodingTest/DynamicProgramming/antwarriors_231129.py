# 입력 1: 첫째 줄에 식량창고 개수 N
# 입력 2: 둘째 줄에 공백 기준으로 각 식량창고에 저장된 식량의 개수 K가 주어진다.
# 출력: 첫째 줄에 개미 전사가 얻을 수 있는 식량 최대 값

# 조건1: 식량창고 일직선
# 조건2: 최소한 한 칸 이상 떨어진 식량창고를 약탈
# 그리드 X
# 구현 X
# 완전탐색 X
# 파라매트릭 서치?

# 1. DP 조건 확인
# DP O

# 2. 변수 파악
n = int(input())
array = list(map(int, input().split()))
# 3. 관계식 정의(점화식)
# 4. 메모하기
# 앞서 계산된 결과를 저장하기 위한 dp table
dp = [0] * 100

# 다이나믹 프로그래밍 진행(Bottom-up / table-filling)
# 5. 기저 상태 파악
dp[0] = array[0]
# 기저 상태 2
dp[1] = max(array[0], array[1])

# 6. 구현하기
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[n-1])
