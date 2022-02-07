# 2178 미로탐색
# N *M 크기의 미로가 주어질 때, (1,1)에서 출발해서 (N,M)까지 이동할 때 지나야 하는 최소 칸 수 출력

# 입력이 노드번호가 아니라 좌표 위치로 주어지면 0,0 -> N-1,M-1로 바꾸기 
#from collections import deque
#띄어쓰기 없이 들어가있다면 split하고 int로 바꾸지 말고 그냥 char형식으로 저장해놓자 
from collections import deque


def solution(arr):
	answer = -1
	N = len(arr)
	M = len(arr[0])
	
	visited = [ [False]*(M) for _ in range(N) ]
	#mirro = [ list(map(int,arr[i].split(''))) for i in range(N)]

	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	dq = deque()
	dq.append( (0,0,1) )
	visited[0][0] = True

	while dq:
		cdis = dq.popleft()
		cx = cdis[0]
		if cdis[0] == N-1 and cdis[1] == M-1:
			answer = cdis[2]
			break
		for k in range(4):
			nx = cdis[0] + dx[k]
			ny = cdis[1] + dy[k]
			if nx < 0 or nx >= N or ny < 0 or ny >= M:
				continue
			if arr[nx][ny] == '1' and visited[nx][ny] == False:
				dq.append( (nx,ny,cdis[2] + 1) )
				visited[nx][ny] = True
	return answer
	

if __name__ == "__main__":
	N,M = map(int,input().split())
	arr = list( input() for _ in range(N) )
	answer = solution(arr)
	print(answer)

	
