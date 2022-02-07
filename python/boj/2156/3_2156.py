def solution(wine):
	N = len(wine)
	dp = [0] * N

	dp[0] = wine[0]
	dp[1] = wine[0] + wine[1]
	dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
	for i in range(3,N):
		dp[i] = max( dp[i-1], dp[i-2] + wine[i], dp )
	
	return dp[N-1]

if __name__ == "__main__":
	N = int(input())
	arr = [ int(input()) for _ in range(N) ]

	answer = solution(arr)

	print(answer)
