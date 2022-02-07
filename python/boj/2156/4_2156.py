def solution(wine):
	N = len(wine)
	dp = [0] * N
    
	dp[0] = wine[0]
	
	for i in range(1,N):
		if i == 1:
			dp[i] = wine[i-1] + wine[i]
		elif i == 2:
			dp[i] = max(dp[i-1], dp[i-2] + wine[i], wine[i-1] + wine[i])           
		else:
			dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3]+wine[i-1]+wine[i])

	return dp[N-1]

if __name__ == "__main__":
	N = int(input())
	arr = [ int(input()) for _ in range(N) ]
	answer = solution(arr)
	print(answer)
