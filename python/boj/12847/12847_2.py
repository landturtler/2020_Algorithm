N,M = map(int,input().split())
pays = list(map(int,input().split()))
answer = 0
dp = [ 0 for _ in range(N)]

dp[0] = pays[0]

for x in range(1,N):
	if x < M:
		dp[x] = dp[x-1] + pays[x]
	else:
	 	dp[x] = max(dp[x-1], pays[x] + dp[x-1] - pays[x-M])

print(dp[N-1])

