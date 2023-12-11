#BFS
# 너비 우선 탐색
# 사용 자료 구조 : 큐를 사용
# 동작구성
# 1. 탐색 시작 노드를 큐에 삽입
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드 중 인접 노드 중 방문하지 않는 노드를 모두 큐에 삽입(일단 반복)
# 더이상 2번 과정을 수행할 수 없을 때 까지 반복

from collections import deque

def bfs(graph, start, visited):
    #큐를 사용한 dfs 구현

    # 1. 시작노드 큐에 삽입
    queue = deque([start])
    visited[start] = True

    #2. 인접한 노드 중 방문하지 않은 노드가 있다면 모두 큐에 삽입(일단 반복)

    #3. 2번 불가할때 까지 반복

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



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

visited = [False] * 9

bfs(graph, 1, visited)

# BFS: Quue에 넣자 마자 True