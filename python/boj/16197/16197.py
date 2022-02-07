#16197 두 동전
# 보드에는 벽,빈공간이 있고 동전 2개가 있고. 버튼을 누를 때마다 두 동전은 같은 방향으로 한 칸이동한다. 두 동전중 하나만 보드에서 떨어뜨리기 위해 최소 몇 번 눌러야 하는지 출력 
# 큐엔 한 값만 넣어야 함. 그래서 여러 값을 넣으려면 list로 넣기
# 만약 큐 안에 여러 타입의 리스트 (ex, 좌표 리스트 + cnt )를 저장할 때 q.append( [arr] + [cnt] )로 해야 함.q.append( arr + [cnt]) XX

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
	dx = [-1,0,1,0]
	dy = [0,1,0,-1]
	
	N,M = map(int,input().split())
	arr = list(['.'] * M for _ in range(N))
	answer = -1
	coins = []
	visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
	
	for i in range(N):
		tmp = input()
		for j in range(M):
			if tmp[j] == 'o':
				coins.append([i,j])
			else:
				arr[i][j] = tmp[j]
	q = deque()
	q.append([coins, 0])
	visit[coins[0][0]][coins[0][1]][coins[1][0]][coins[1][1]] = True
	while q :
		cur = q.popleft()
		coin1 = cur[0][0]
		coin2 = cur[0][1]
		cnt = cur[1]
		if cnt > 10:
			break
		for k in range(4):
			nx1 = coin1[0] + dx[k]
			ny1 = coin1[1] + dy[k]
			nx2 = coin2[0] + dx[k]
			ny2 = coin2[1] + dy[k]
				
			# 둘 다 범위를 벗어난 경우 제외
			if (nx1 < 0 or nx1 >= N or ny1 < 0 or ny1 >= M) and (nx2 < 0 or nx2 >=N or ny2 < 0 or ny2 >=M):
				continue
			
			# 둘 다 범위 내에 있는 경우 이동 후 큐에 삽입 
			elif nx1 >= 0 and nx1 < N and ny1 >= 0 and ny1 < M and nx2 >= 0 and nx2 < N and ny2 >=0 and ny2< M:
				if arr[nx1][ny1] == '#':
					nx1 = coin1[0]
					ny1 = coin1[1]
					
				if arr[nx2][ny2] == '#':
					nx2 = coin2[0]
					ny2 = coin2[1]
				
				if visit[nx1][ny1][nx2][ny2] == False:
					visit[nx1][ny1][nx2][ny2] = True
					q.append([[[nx1,ny1],[nx2,ny2]], cnt+1])
			
			#둘 중 하나만 범위 내에 있는 경우 출력 
			else:
				answer = cnt + 1
				q.clear()
				if answer > 10:
					answer = -1
				break
	
	print(answer)		
