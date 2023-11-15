

N = int(input())
travel_plan = input().split()



# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

directions = ['R', 'U', 'L', 'D']
def solution(travel_plan, N):
    # 마지막 출력 때는 1씩 올려 주어야 한다.
    current_point = [1,1]
    x = current_point[0]
    y = current_point[1]
    for char in travel_plan:
        for i in range(len(directions)):
            if char == directions[i]:
                x += dx[i]
                y += dy[i]

        if x < 1 or x > N or y < 1 or y > N:
            continue
        else:
            current_point[0] = x
            current_point[1] = y

    return current_point


print(solution(travel_plan, N))