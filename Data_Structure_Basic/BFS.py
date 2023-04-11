from collections import deque
# 1. 방문 노드 기록 리스트 표시(1차원)
# 2. 각 노드의 연결 정보 리스트(2차원)

# BFS는 큐에 들어온 순서대로 pop을 하면 방문 순서가 된다.
# BFS 메서드 정의

from collections import deque
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque라이브로리 사용
    # 시작 노드 큐 삽입
    queue = deque([start])

    # 방문 처리
    visited[start] = True

    #큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS,BFS 함수 호출
bfs(graph, 1, visited)
