from collections import deque
# 문제풀이
# 1. [0, 0]에서 시작
# 2. BFS 사용 - 최단 경로
# 3. 큐가 빌때 까지 반복
#BFS 소스 구현

N, M = list(map(int, input().split()))
graph = []
for i in range(N):
    graph.append(list(map(int,input())))


dx = [-1, 0, 1, 0] #하 좌 상 우
dy = [0, -1, 0, 1]

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

        #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N-1][M-1]


print(bfs(0,0))
