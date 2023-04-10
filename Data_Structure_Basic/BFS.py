from collections import deque
# 1. 방문 노드 기록 리스트 표시(1차원)
# 2. 각 노드의 연결 정보 리스트(2차원)

# BFS 메서드 정의

def bfs(graph, v, visited):
    # 현재 노드 큐에 삽입





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

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)