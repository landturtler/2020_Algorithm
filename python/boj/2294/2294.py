#2294 동전2
#N개의 동전을 이용하여 합을 K로 만들때 최소한의 동전 개수는?
# dp[i] : 합을 i로 만들 수 있는 경우의 수 중, 최소한의 동전 개수, dp[i] = dp[i-coins] + 1

import sys

N, K = map(int,input().split())
coins = list(int(input()) for _ in range(N))
dp = [sys.maxsize] * (K+1) #합을 i로 만들 수 있는 경우 수 중, 최소 동전 개수

#입력받은 동전값 초기화
for coin in coins:
	dp[coin] = 1

for coin in coins:
	for i in range(coin+1,K+1):
		dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[K])

