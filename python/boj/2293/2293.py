#2293 동전1
# N개의 동전들을 가지고 합이 K로 만들 수 있는 경우의 수
# 처음엔 dfs라 생각했지만 반복해서 사용할 수 있음에 유의
# 10원을 만들기 위해서 5 + 5가 되고, 또 5 = 1+2+2가 될 수 있다.
# 1원으로 만들 수 있는 경우의 수 구하고,2원으로 만들수있는 경우의 수 더하고,...
#dp[j] = dp [j](이전 동전 종류를 이용해 j를 만들었던 경우의 수 ) + dp[j-coins[i]]( 새 동전을 사용하는 경우 추가)

if __name__ == "__main__":
	N, K = map(int,input().split())
	coins = list ( int(input()) for _ in range(N))
	dp = [0] * (K+1)
	
	dp[0] = 1 # 동전 1개로 사용하는 경우
	
	for coin in coins:
		for i in range(coin,K+1):
			dp[i] += dp[i-coin]
	
	print(dp[K])
