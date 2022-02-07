#dfs와 bfs
#정점 개수 N, 간선 개수 M, 탐색 시작 정점 번호 V, 간선이 연결하는 두 정점번호가 주어질 때 첫째 줄에 dfs 결과를 그 다음 줄엔 bfs를 출력하라 ( v부터 방문된 점을 순서대로  출력)
from collections import deque


def bfs(x,y):
	q = deque((x,y))
	while q:
	 cdir = q.popleft()
	 print(cdir, end = " ")

	for k in range(4):
		nx = cdir[0] + dx[k]
		ny = cdir[1] + dy[k]
		if nx < 0 || nx >= N || ny < 0 || ny >= N ||b_visited[nx][ny] == True:
			continue
		q.append((nx,ny))
		visited[nx][ny] = True

def dfs(x,y):
	d_visited[x][y] = True
	print(
		

if __name__ == "__main__":
	N,M,start = map(int,input().split())
	arr = [ [False]* N for _ in range(N) ]
	
	for i in range(M):
		a,b = map(int,input().split())
		arr[a][b] = True
		arr[b][a] = True

	d_visited  = [[False] * N for _ in range(N)]
	b_visited = [[False] * N for _ in range(N)]

	#dfs


	#bfs
	for i in range(N):
		for j in range(N):
			if b_visited[i][j] == False and arr[i][j] == True:
				b_visited[i][j] = True
				bfs(i,j)

