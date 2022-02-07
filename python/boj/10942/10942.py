#10942 팰린드롬
#dp[s][e] = 펠린드롬인지를 저장하는 dp 배열. 길이가 1이면 무조건 1, 길이가 3이상이면 S와 E가 같은 수이고 DP[S + 1][E - 1]이 1이면 1)
# 헷갈린 것 : [0] for _ in range(N)과 [ 0 for _ in range(N)] 주의할것 

import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	dp = [ [0 for _ in range(N)] for _ in range(N)]

	#길이가 1
	for i in range(N):
		dp[i][i] = 1

	#길이가 2
	for i in range(N - 1):
		if arr[i] == arr[i + 1]:
			dp[i][i + 1] = 1
	
	#길이가 3이상 : dp[s + 1][e - 1]이 1이고 s와 e가 같으면  1  
	for i in range(2,N):
		for j in range(N-i):
			if arr[j] == arr[j + i] and dp[j + 1][i + j - 1] == 1:
				dp[j][i + j] = 1
	
	M = int(input())
	for _ in range(M):
		a, b = map(int,input().split())
		print(dp[a - 1][b - 1])

	
		
