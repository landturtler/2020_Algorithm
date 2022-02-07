#12865 평범한 배낭
# 여행에 필요한 N개 물건이 있다. 각 물건은 무게 W와 가치 V를 가진다. 최대 K만큼의 무게만을 넣을 수 있을 때, 배낭에 넣을 수 있는 물건 가치의 최댓값은?
# dp[i][j] : 처음부터 i번까지의 문제를 살펴보고, 배낭 용량이 j일때 배낭에 들어갈 물건의 최대 가치 
# dp[i][j] = if w[i] > j  dp[i-1][j]  #i번재 물건의 무게가 j보다 크면 무조건 i번쨰 물건 안넣음.i-1번째까지 고려한 최대값 넣음 
#			else max( dp[i-1][j], dp[i-1][j-w[i]] + w[i] ) #i번째 물건을 넣지 않았을 때랑, i번째 물건 넣었을 때 최대값 넣음)


import sys
input = sys.stdin.readline

def solution(N,K,things):
	
	#things를 무게 순으로 정렬 
	things.append((0,0))
	things.sort()
	
	dp = [ [0] * (K+1) for _ in range(N+1) ] #dp[i][j] : i번째 물건까지 살펴봤을 때, 용량이 j인 배낭에 들어갈 최대 가치 
	
	for i in range(1,N+1):
		for j in range(K+1):
			if things[i][0] > j:
				dp[i][j] = dp[i-1][j]

			else:
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-things[i][0]] + things[i][1] )
	return dp[N][K]

if __name__== "__main__":
	N,K = map(int,input().split())
	things = [ tuple(map(int,input().split())) for _ in range(N) ]

	answer = solution(N,K,things)
	print(answer)
