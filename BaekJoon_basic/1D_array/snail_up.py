# V: 막대의 높이
# A : 아침 올라가는 거리
# B : 밤에 내려오는 거리

# 조건 : 1 ≤ B < A ≤ V ≤ 1,000,000,000

A, B, V = list(map(int,input().split()))

dis_per_day = A-B # 하루 올라가는 거리
dis_except_last_day = V-A #마

day_count = dis_except_last_day // dis_per_day

if day_count == 0:
    day_count += 1
day_count += 1

print(day_count)




