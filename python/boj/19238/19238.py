'''
19238 스타트택시

접근 방식 :BFS지만 모든 승객을 탐색하면 시간초과가 나므로, 현재 위치에서 가장 가까운 승객을 찾아가는 조건을 잘 추가해야 함

'''

import sys
from collections import deque
import heapq

input = sys.stdin.readline
INF = 1e9

dirx = [-1,0,1,0]
diry = [0,1,0,-1]
N = 0

#현재 기준 가장 가까운 승객의 위치와 승객 위치까지의 거리를 return하는 함수 
def findPerson(tx,ty):
	global dirx,diry,N
	hq = [] #우선순위 큐.최단 경로 승객 리스트들 
	q = deque()
	q.append([tx,ty,0])

	visited = [[False] * N for _ in range(N)]
	visited[tx][ty] = True
	min_dis = INF

	while q:
		cx, cy, dis = q.popleft()
		if min_dis < dis:
			break

		#최단 경로 손님을 찾았을 때 
		elif board[cx][cy] >= 1:
			heapq.heappush(hq,[cx,cy])
			min_dis = dis

		#이동 
		else:
			for i in range(4):
				nx,ny = cx + dirx[i], cy + diry[i]
				if nx < 0 or nx >= N or ny < 0 or ny >= N:
					continue

				if board[nx][ny] != -1 and not visited[nx][ny]:
					visited[nx][ny] = True
					q.append([nx,ny,dis+1])
		
	#만약 최단경로 승객이 여러명이면 행/열이 작은 승객을 리턴 
	if len(hq) > 0:
		x,y = heapq.heappop(hq)
		return([x,y,min_dis])

	else:
		return -1

#최단거리 손님을 태우고 목적지까지 갈 수 있으면 해당거리 리턴, 만약 갈수 없으면 -1 리턴 
def moveTaxi(sx,sy,dx,dy):
	global N,dirx,diry
	q = deque()
	q.append([sx,sy,0])
	visited = list([False] * N for _ in range(N))
	visited[sx][sy] = True

	while q:
		cx,cy,dis = q.popleft()
		
		if cx == dx and cy == dy:
			return dis

		for i in range(4):
			nx = cx + dirx[i]
			ny = cy + diry[i]

			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue

			if board[nx][ny] != -1 and not visited[nx][ny]:
				q.append([nx,ny,dis+1])
	return -1
			

if __name__ == "__main__":	
	N,M,fuel = map(int,input().split())
	board = []
	for i in range(N):
		tmp = list(map(int,input().split()))
		for j in range(len(tmp)):
			if tmp[j] == 1:
				tmp[j] = -1
		board.append(tmp)				
	tx,ty = map(int,input().split())
	tx,ty = tx-1,ty-1
	
	#승객 정보 저장
	idx= 1 #각 승객의 id값 
	st = {} #승객의 id가 key, 시작 좌표가 value
	des = {} #승객의 id가 key, 도착 좌표가 value
	for _ in range(M):
		sx,sy,dx,dy = map(int,input().split())
		board[sx-1][sy-1] = idx
		st[idx] = [sx-1,sy-1]
		des[idx] = [dx-1,dy-1]
		idx +=1
	
		  
	#택시 운행 시작 
	flag = True #택시 운행을 정상종료했는지를 판단하는 flag 
	for _ in range(M):
		tmp = findPerson(tx,ty)
		person = [tmp[0],tmp[1]] #가장 가까운 승객 위치 
		dis_st = tmp[2] #현재 택시 위치~승객까지 이동 거리 
		
		#최단 거리에 존재하는 승객이 없으면 운행 종료  
		if person == -1:
			flag = False
			break
		
		#최단 거리 승객을 찾았으면 해당 승객의 index를 찾고 이동할수 있는지 판단  
		idx = board[person[0]][person[1]]
		dis_des = moveTaxi(st[idx][0], st[idx][1], des[idx][0], des[idx][1])

		#목적지까지 갈 수 있는 연료가 부족하거나,목적지까지 갈 수 없으면 운행 종료  
		if dis_des == -1 or fuel < (dis_des + dis_st):
			flag = False
			break

		#목적지까지 갈 수 있으면 연료 충전 후, board에서 방금 옮겼던 승객 번호 삭제
		fuel += (dis_des - dis_st)
		board[person[0]][person[1]] = 0
		tx = des[idx][0]
		ty = des[idx][1]

	if flag:
		print(fuel)
	else:
		print("-1")
