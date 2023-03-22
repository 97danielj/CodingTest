# V: 막대의 높이
# A : 아침 올라가는 거리
# B : 밤에 내려오는 거리

# 조건 : 1 ≤ B < A ≤ V ≤ 1,000,000,000

def solve(A, B, V):
    dis_per_day = A - B  # 하루 올라가는 거리
    V = V - B # 정상에 도달하고 밤에 미끄러지 않는 거리

    past_days = V // dis_per_day # 1 총 거리//하루 가는 거리
    rest_dis = V % dis_per_day # 2 # 남는 거리

    #if rest_dis != 0: #남은 거리가 0이 아니면 내려와서 하루 더 자야 한다.
    past_days += 1

    return past_days


A, B, V = list(map(int,input().split()))

print(solve(A, B, V))





