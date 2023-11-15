#음료수 얼려먹기

# 입력 : NxM 크기의 엄음 틀
# 출력 : 만들 수 있는 아이스크림 개수

#문제해결
# 노드 위치
# DFS에서 모두 방문처리
# result에는 아이스크림 개수 저장

#연결 요소 찾기 => DFS

N, M = list(map(int, input().split()))
graph = [list(map(int,input().split())) for _ in range(N)]

def dfs(x, y):
    # 현재 위치 노드가 범위를 벗어나면
    if x<=-1 or x>= N or y<=-1 or y>= M:
        return False

    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True #아이스크림을 만족했다.
    return False

result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)


