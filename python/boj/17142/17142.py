#17142 연구소3
# 문제 : N*N크기 연구소는 빈칸,벽,바이러스로 이루어져있다. 그 중 M개의 바이러스를 활성상태로 변경할 때 모든 빈칸에 바이러스를 퍼뜨리는 최소시간은?
# 알고리즘: BFS / 구현
# 새로 알게된 것 : from copy import deepcopy / 2차원 배열 최댓값 : max(map(max,arr))
# 고민했던 것 : 해당 지점까지 퍼지는데 걸리는 시간을 visited 배열에 넣을지/ map배열에 넣을지 

import sys
input = sys.stdin.readline
from copy import deepcopy
from itertools import combinations
from collections import deque
INF = int(1e9)
min_time = INF
arrs = [] #연구소
dir = [[-1,0], [0,1], [1,0], [0,-1]]

def bfs(virus,cnt):
	global min_time, dir, arrs
	visited =[[-1] * N for _ in range(N)]
	q = deque()
	for vir in virus:
		q.append(vir)
		visited[vir[0]][vir[1]] = 0
	
	while q:
		cx, cy = q.popleft()
		tim = visited[cx][cy]
		#탐색 시간이 이전의 최소 시간보다 오래 걸리거나 모든 빈칸을 다 퍼뜨렸으면 break
		if tim > min_time or cnt == 0:
			break
		for i in range(4):
			nx = cx + dir[i][0]
			ny = cy + dir[i][1]
			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			#빈칸이거나 비활성 바이러스이면 퍼뜨림 
			if visited[nx][ny] == -1 and arrs[nx][ny] != 1:
				visited[nx][ny] = visited[cx][cy] + 1
				q.append((nx,ny))
				if arrs[nx][ny] == 0:
					cnt -= 1								
	#bfs 탐색 후, 모든 빈칸에 바이러스가 퍼졌는지 확인(기존의 비활성 바이러스는 고려 X)
	if cnt == 0:
		min_time = min(min_time,max(map(max,visited)))


if __name__ == "__main__":
	N,M = map(int,input().split())
	virus = [] #바이러스의 좌표
	blank = 0 #빈칸 개수

	#연구소 정보 저장
	for i in range(N):
		tmp = list(map(int,input().split()))
		arrs.append(tmp)
		for j in range(N):
			if tmp[j] == 2:
				virus.append((i,j))
			elif tmp[j] == 0:
				blank += 1

	# 바이러스를 선택하는 경우의 수 
	comb_list = list(combinations(virus,M))
	for comb in comb_list:
		bfs(comb,blank)
	
	if min_time == INF:
		print('-1')
	else:
		print(min_time)

	
