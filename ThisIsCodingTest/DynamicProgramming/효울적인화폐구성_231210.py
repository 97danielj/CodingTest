
# 입력 1: N, M
# 입력 2: N개의 화폐단위

# 출력 1: M원을 만들 수 있는 화폐 최소 단위
# M<100000 => nlogn

n, m = map(int, input().split())
array = [0] * n #화폐 단위가 저장

for i in range(n):
    array[i] = int(input())

# 4. 메모하기
dp = [100001] * (m+1)

# 5. 기저 상태 파악
dp[0] = 0

# 6. 구현하기
for i in range(1, m+1):
    for j in range(len(array)):
        if i >= array[j] and dp[i - array[j]] != 100001: #(i-k)원을 만드는 방법이 존재하는 경우
            dp[i] = min(dp[i], dp[i-array[j]]+1)

# 최종적으로 M원을 만드는 방법이 존재하는 경우
if dp[m] != 100001:
    print(dp[m])
else:
    print(-1)