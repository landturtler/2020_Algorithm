#녹색 옷 입은 애가 젤다지?
#다익스트라는 간선 길이가 핵심( 특정 노드 사이의 거리)
#얜 간선의 길이가 아니라 그 "노드"로 가는 비용
#얘를 다익스트라로 N * M * 4(상하좌우) 크기로 넣어주어ㅑ 함

from heapq import heappush, heappop
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1

def bfs():
	q = []
	heapq.heappush(q,(graph[0][0],0,0))
	distance[0][0] = 0

	while q:
		cost, x, y = heapq.heappop(q)

		if x == (N-1) and y == (N-1):
			print(f'Problem {cnt}: {distance[x][y]}')
			break

		for i in range(4):
			nx = x + dx[i]
			ny = y _ dy[i]

			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				nc = cost + graph[nx][ny]

				if nc < distance[nx][ny]:
					distance[nx][ny] = nc
					heapq.heappush(q,(nc,nx,ny))
cnt = 1

while True:
	N = int(input())
	if N == 0:
		break
	
	graph = [ list(map(int, input().split())) for _ in range(N)]
	distance = [ [INF] * N for _ in range(N)]
	dijkstra()
	cnt += 1





