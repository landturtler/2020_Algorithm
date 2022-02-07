#실전 5_3. 음료수 얼려먹기

#입력받기
N,M = map(int,input().split())
cnt = 0

global board
global visited

board = [0 for _ in range(N)]
visited = [ [0] * M for _ in range(N)]

#띄어쓰기 없이 입력받을 경우, 떼는 법

for i in range(N):
	board[i] = list(map(int, input()))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

#dfs 함수 구현
def dfs(y, x):
	visited[y][x] = 1

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ny][nx] == 1:
			continue
		dfs(ny,nx)

#모든 노드에 대해 dfs 수행
for y in range(N):
	for x in range(M):
		if board[y][x] == 0 and visited[y][x] == 0:
			cnt += 1
			dfs(y,x)

print(cnt)
