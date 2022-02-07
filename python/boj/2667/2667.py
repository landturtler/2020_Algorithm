#2667
#bfs
#collection이 아니라 뒤에 s붙음 
#leftpop 이 아니라 popleft 
#main함수에서 글로벌 변수 쓸 떈 global 안붙임?
from collections import deque
visited = []
mirro = []
N = 0

def bfs(i,j,idx):
	global N
	cnt = 0
	dx = [ -1,0,1,0]
	dy = [0,1,0,-1]

	dq = deque()
	dq.append( (i,j) )
	visited[i][j] = idx
	while dq:
		cur = dq.popleft()
		cnt += 1
		for k in range(4):
			nx = cur[0] + dx[k]
			ny = cur[1] + dy[k]

			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			if visited[nx][ny] == -1 and mirro[nx][ny] == '1':
				visited[nx][ny] = idx
				dq.append( (nx,ny) )
	return cnt

def solution(arr):
	answer = []
	global visited,mirro,N

	visited = [ [-1] * N for _ in range(N) ]
	mirro = arr.copy()

	idx = 1
	for i in range(N):
		for j in range(N):
			if visited[i][j] == -1 and arr[i][j] == '1':
				answer.append( bfs(i,j,idx) )
				idx += 1

	answer.sort()
	return answer


if __name__ == "__main__":
	N = int(input())
	arr = [ input() for _ in range(N)]

	answer = solution(arr)
	print(len(answer))
	for x in answer:
		print(x)

