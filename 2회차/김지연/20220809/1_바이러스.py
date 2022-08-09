from pprint import pprint

C = int(input()) 
N = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
graph = [[]*C for _ in range(C+1)] # (인접행렬) 정점의 갯수만큼 생성

for _ in range(N):
    u, v = map(int, input().split()) # 간선의 양 끝점 u, v
    graph[u].append(v) # 인접 리스트
    graph[v].append(u)

cnt = 0
visited = [0]*(C+1)
def dfs(start):
    global cnt # 함수에 사용된 cnt는 지역변수라서 함수 바깥의 영역에서 호출하려면 global 선언 필요
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)