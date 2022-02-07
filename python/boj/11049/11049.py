#11049 행렬 곱셈 순서
# 크기가 N*M인 행렬 A와 크기가 M*K인 행렬 B를 곱할 때 필요한 연산 수는 N*M*K이다. 같은 곱셈이지만 곱셈을 하는 순서에 따라 곱셈 연산 수가 달라진다. 행렬 N개의 크기가 주어졌을 때 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값?

import sys
input = sys.stdin.readline
INF = sys.maxsize
dp = []

def go(start,end):
	if start == end:
		return 0

	elif dp[start][end] != INF:
		return dp[start][end]
	
	else:
		for i in range(start,end):
			dp[start][end] = min( dp[start][end], go(start,i) + go(i+1,end) + arr[start][0]*arr[i+1][0]*arr[end][1])
		
		return dp[start][end]

if __name__ == "__main__":
	N = int(input())
	arr = list(tuple(map(int,input().split())) for _ in range(N))
	#dp[i][j]: i번째~j번째 행렬까지 곱하는데 필요한 연산 횟수의 최솟값
	dp = [[INF for _ in range(N)] for _ in range(N)] 
	
	#인접한 2개의 행렬은 미리 곱하기
	for i in range(N-1):
		dp[i][i+1] = arr[i][0]*arr[i+1][0]*arr[i+1][1]
		dp[i][i] = 0
	dp[N-1][N-1] = 0

	answer= go(0,N-1)
	print(answer)
	
