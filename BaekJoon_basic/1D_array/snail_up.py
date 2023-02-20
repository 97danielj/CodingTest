# V: 막대의 높이
# A : 아침 올라가는 거리
# B : 밤에 내려오는 거리


A, B, V = list(map(int,input().split()))

point = 0
day_count = 0
while True:

    if point+A >= V:
        day_count +=1
        break

    point += (A-B)
    day_count += 1


print(day_count)


