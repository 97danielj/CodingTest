
# 입력 조건1: N
# 입력 조건2: 각 병사의 전투력

# 출력1: 첫째줄에 남아있는 병사의 수가 최대가 되도록하기 위해 열외시켜야 하는 병사의 수

# 조건: 내림차순&병사의 수 최대

# 문제해결아이디어: 가장 긴 증가하는 부분수열(LIS) => 가장 긴 감소하는 부분 수열을 찾는 문제로 치환
# LIS를 조금 수정한다.


n = int(input())

array = list(map(int, input().split()))
#순서를 뒤집어 '최장 부분 수열'문제로 변환
array.reverse()

# 다이나믹 프로그래밍(메모)
dp = [1] * n

# 가장 긴 증가하는 부분 수열 알고리즘 수행
for i in range(1, n):
    for j in range(0, i): #점화식을 떠올려
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수 를 출력
print(n - max(dp))
# max(dp)는 가장 긴 증가하는 부분수열의 문제


