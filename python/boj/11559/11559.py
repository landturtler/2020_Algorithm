#11559 puyo puyo
# 문제: 같은 색의 뿌요가 4개이상 상하좌우로 있으면 1연쇄가 발생, 만약 터질수있는 부요가 여러 그룹이 있으면 동시에 터져야 하고, 1연쇄로 판단. 터진 뿌요의 자리에 그 위에있던 뿌요들은 중력의 영향을 받아 아래로 떨어지고 다시 연쇄가 발생할 수 있음
# 필드가 주어졌을떄 연쇄가 몇 번 일어날지 계산하라
# 알고리즘 : bfs, 구현
# 실수한 것 : 띄어쓰기 없이 입력받는 경우, string형 그대로 입력받을 수 있으나 arr[i][j] 처럼 인덱스로 접근이 불가능함. 따라서 입력받을 때 list(input().rstrip())으로 list로 변경하기 
# 처음안 것 : 중력에 의해 떨어지는 함수 작성 시, 큐 사용하기 

from collections import deque
import sys 
input = sys.stdin.readline
arrs = []
dir = [ [-1,0], [0,1], [1,0],[0,-1] ]
N = 12
M = 6

#터진 이후 중력에 의해 내려감
# 탐색은 가장 마지막 줄부터 시작
def go_down():
	global arrs
	for j in range(M):
		q = deque()
		for i in range(N-1,-1,-1):
			if arrs[i][j] != '.':
				q.append(arrs[i][j])
		for i in range(N-1,-1,-1):
			if q:
				arrs[i][j] = q.popleft()
			else:
				arrs[i][j] = '.'
	
#bfs
def puyo():
	global N,M
	flag = False #연쇄가 발생했는지 판단 
	for i in range(N):
		for j in range(M):
		 	#bfs 
			if arrs[i][j] != '.':
				visited = [ [False] * M for _ in range(N)]
				visited[i][j] = True
				q = deque()
				q.append([i,j])
				cnt = 1

				while q:
					cx,cy = q.popleft()
					for k in range(4):
						nx = cx + dir[k][0]
						ny = cy + dir[k][1]
						if nx < 0 or nx >= N or ny < 0 or ny >= M:
							continue
						if visited[nx][ny] == False and arrs[cx][cy] == arrs[nx][ny]:
							q.append([nx,ny])
							visited[nx][ny] = True
							cnt += 1
				#연쇄 발생 
				if cnt >= 4:
					flag = True
					for i in range(N):
						for j in range(M):
							if visited[i][j] == True:
								arrs[i][j] = '.'

	if flag == True:
		go_down()
		return True

	else:
		return False
	
if __name__ == "__main__":
	arrs = list(list(input().rstrip()) for _ in range(N))
	answer = 0

	while 1:
		flag = puyo()
		if flag == False:
			print(answer)
			break
		else:
			answer += 1

