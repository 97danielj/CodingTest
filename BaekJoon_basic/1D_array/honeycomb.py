# 벌집이동을 위한 필요한 최소 경로

# n=1, 2, 3 이렇게 올라가는데 정해진 규칙이 있을 것 이다.
# n=1, 1
# n=2, 2~7 / 6개
# n=3, 8~19 : 12개
# n=4, 20~37 / 18개
# n에 따른 등비수열을 이루고, 급수를 이룬다.
#우리 N에 대한 수식에서 n을 구한다.
N = int(input())
n = 0
sum_seq = 0
while True:
    if n == 0: # 첫 번재 원소
        GS = 1
    else:
        GS = n * 6 #다음 원소
    sum_seq += GS

    if sum_seq >= N:
        break
    n += 1

print(n+1)


