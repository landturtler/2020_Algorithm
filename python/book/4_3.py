#게임 개발

#반시계 방향 
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#입력 받기
N,M = map(int,input().split())
x,y,direction = map(int,input().split())
board =  [ 0 for _ in range(N)] 

# 1: 바다 , 0 : 육지 
for i in range(N):
	board[i] = list(map(int,input().split()))  

board[x][y] = 1 #시작 부분 방문 처리
count = 1 #캐릭터가 방문한 칸의 수. 맨 처음 포함

# 캐릭터 이동(반시계 방향) 
while True:
	newdirection = direction
	for i in range(1,4):
		nx = x + dx[ (4 + (direction - i)) % 4] 
		ny = y + dy[ (4 + (direction - i)) % 4] 
		
		if nx < 0 or nx >= M or ny < 0 or ny >= N or board[nx][ny] == 1 :
			continue
		
		#네 방향 중 이동할 곳을 찾음
		newdirection =  (4 + (direction - i)) % 4	
		x = nx
		y = ny
		board[nx][ny] = 1
		break 
	
	#더 이상 이동할 수 없음 
	if newdirection == direction:
		break
	else:
	 direction = newdirection
	 count += 1

print(count)


