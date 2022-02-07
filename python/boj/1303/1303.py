#1303 전쟁-전투
#우리편은 W,상대편은B일때 우리 병사 합과 적국 병사 합을 구하라. 병사는 모일수록 N^2만큼 위력을 낼 수 있다.
# sys.stdin.readline쓰면 \n도 같이 들어감.없애려면 strip()쓰기 
#input()에서는 string을 입력받기 위해선 ""을 붙여야 함. 큰따옴표를 안붙이면 변수명이 입력
import sys
from collections import deque
input = sys.stdin.readline

visited = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N= 0
M = 0

def bfs(x,y,ch):
	global visited, our_team,your_team 
	q = deque()

	visited[x][y] = True
	cnt = 1
	q.append((x,y))

	while q:
		cur = q.popleft()
		for k in range(4):
			nx = cur[0] + dx[k]
			ny = cur[1] + dy[k]
			if nx < 0 or nx >= M or ny <0 or ny >= N:
				continue
			if visited[nx][ny] == False and arr[nx][ny] == ch:
				cnt += 1
				q.append((nx,ny))
				visited[nx][ny] = True

	return cnt*cnt

def solution(N,M):
	global visited,our_team,your_team
	answer = []
	visited = list( [False] * N for _ in range(M) )
	our_team = 0
	your_team = 0

	for x in range(M):
		for y in range(N):
			if visited[x][y] == False:
				if arr[x][y] == 'W':
					our_team += bfs(x,y,arr[x][y])
				else:
					your_team += bfs(x,y,arr[x][y])

	answer.append(our_team)
	answer.append(your_team)
	return answer

if __name__ == "__main__":
	N,M = map(int,input().split()) #가로 N 세로 M
	arr = [list(input().strip()) for _ in range(M)]

	answer = solution(N,M)

	for x in answer:
		print(x, end = " ")
