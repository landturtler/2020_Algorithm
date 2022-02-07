#(0,0) -> (N-1,N-1)로 가는 법. dfs로 가도 되는데 visited를 쓸 수 없음. dp로도 풀 수 있음
#대각선 아래 오른쪽 
# 2차원 리스트 입력받을 때!!! list( list(map(int,input().split())) for_in range(N)) -- list 2번 써야 함/ 안그러면 2차원 배열에 제대로안들어감..! 

import sys
input = sys.stdin.readline

arr = []
N = 0
cnt = 0

def dfs(x,y,d):
	global arr,N,cnt
	if x == N-1 and y == N-1:
		cnt += 1
		return

	#대각선 
	if d == 0:
		if x+1 < N and y+1 < N and arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
			dfs(x+1,y+1,0)
		if x+1 < N and y < N and arr[x+1][y] == 0:
			dfs(x+1,y,1)
		if x < N and y+1 < N and arr[x][y+1] == 0:
			dfs(x,y+1,2)
	
	elif d == 1:
		if x+1 < N and y+1 < N and arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
			dfs(x+1,y+1,0)
		if x+1 < N and y< N and arr[x+1][y] == 0:
			dfs(x+1,y,1)

	elif d == 2:
		if x+1 < N and y+1 < N and arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
			dfs(x+1,y+1,0)
		if x < N and y+1 < N and arr[x][y+1] == 0:
			dfs(x,y+1,2)


def solution(tmp):
	global arr
	
	arr = tmp.copy()
	dfs(0,1,2) #0,0을 1번으로 가기 
	
	return(cnt)

if __name__ == "__main__":
	
	N = int(input())
	
	tmp = list( list(map(int,input().split())) for _ in range(N))

	answer = solution(tmp)
	print(answer)

