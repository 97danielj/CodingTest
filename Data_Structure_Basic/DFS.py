# 두가지 자료가 있어야 한다.
# 1. 그래프 연결 정보 리스트(2차원)
# 2. 방문 기록 리스트 (1차원)

# DFS는 들어온 스택에 들어온 순서
def dfs(graph, v, visited):
    # 현재 노드(탑노드) 방문 처리
    visited[v] = True
    print(v, end = " ")

    # 인접 노드 탐색
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)




# 각 노드가 연결된 정보를 표현(2차원 리스트)

graph = [
    [],
    [2, 3, 8], # 1번 노드와 연결
    [1, 7], # 2번 노드와 연결
    [1, 4, 5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)

visited = [False] * 9

dfs(graph, 1, visited)