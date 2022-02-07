def solution(wine):
	N = len(wine)
	dp = [ [0,0,0] for _ in range(N) ]
	dp[0][1] = wine[0]

	for i in range(1,N):
		dp[i][0] = max (dp[i-1][0], dp[i-1][1], dp[i-1][2] )
		dp[i][1] = max(dp[i-1][0] + wine[i], dp[i-1][1])
		dp[i][2] = max(dp[i-1][1] + wine[i], dp[i-1][2])
	return max( dp[N-1][0], dp[N-1][1], dp[N-1][2])


if __name__ == "__main__":
	N = int(input())
	arr = [ int(input()) for _ in range(N) ]
	answer = solution(arr)
	
	print(answer)

