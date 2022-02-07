from itertools import accumulate

N,M = map(int,input().split())
pays = list(map(int,(input().split())))
sum_list = list(accumulate(pays))
dp = [0] * N

for x in range(N):
	if x < M:
		dp[x] = sum_list[x]
	else:
		dp[x] = max(dp[x-1],sum_list[x] - sum_list[x-M])

print(dp[N-1])

