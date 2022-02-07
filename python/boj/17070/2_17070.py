#dp로 푸는 방법
#(0,0) -> (N-1,N-1)로 가는 방법은 dp로도 풀 수 있다. 작은 문제로 나눌 수 있고,memoization이 되기 때문

#포도주시식처럼 dp[x][y][d]로 저장하기( (x,y)를 d방향으로 오는데 가능한 경우의 수 )

import sys
input = sys.stdin.readline

def solution(N,arr):

	dp = [list( [0]*3 for _ in range(N)) for _ in range(N)]
	#초기화 (d: 0 (대각선) 1(우측) 2(아래) )
	dp[0][1][1] = 1

	for x in range(N):
		for y in range(N):
			#대각선 확인
			if x-1 >= 0 and y-1 >=0 and arr[x-1][y-1] == 0 and arr[x][y-1] == 0 and arr[x-1][y] == 0:
				dp[x][y][0] += ( dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2])

			#우측 확인
			if y-1 >= 0 and arr[x][y-1] == 0:
				dp[x][y][1] += ( dp[x][y-1][1] + dp[x][y-1][0] )
			
			#아래측 확인
			if x-1 >= 0 and arr[x-1][y] == 0:
				dp[x][y][2] +=( dp[x-1][y][2] + dp[x-1][y][0])
	
	if arr[N-1][N-1] == 0:
		return sum(dp[N-1][N-1])
	else:
		return 0

if __name__ == "__main__":
	N = int(input())
	tmp = list(list(map(int,input().split())) for _ in range(N))

	answer = solution(N,tmp)
	print(answer)
