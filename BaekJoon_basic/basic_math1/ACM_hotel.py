t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1 # 가로 이동 거리, 방번호
    floor = n % h  # 위로 이동거리, 층 번호
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')