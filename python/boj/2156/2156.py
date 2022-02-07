#2156 포도주시식
# top-down / bottom-up 방식으로 풀기
# dp배열엔 i줄까지 마셨을때 최대 포도주 양 정보 + 몇 번째 연속으로 마셨는지 정보를 알고 있어야 함 => 2차원 배열로 생성하기(포도주양,연속으로 몇번째 마셨을때 인지)
# bottom_up일때 dp[i][0]이 헷갈림: 
# top-down에서 메모리제이션 꼭 하기!
MAX = 10001
dfs_dp[MAX][3]
def dfs(idx,cnt,wine):
	if idx < 0:
		return 0
	elif dp[idx][cnt] != -1:
		return dp[idx][cnt]
	
	else:
		if cnt > 0:
			dp[idx][cnt] = dfs(idx-1,cnt-1) + wine[idx]
		else:
			dp[idx][cnt] = max( dfs(idx-1,0), dfs(idx-1,1), dfs(idx-1,2) )
		return dp[idx][cnt]


def solution(wine):
	####top_down######
	N = len(wine)
	for i in range(MAX):
		for j in range(3):
			dfs_dp[i][j] = -1
	
	return dfs(N,0)
	

   #####bottom_up1#####
	N = len(wine)
	dp = [0,0,0] * N #dp[i][j] : i줄까지 마셨을때 마실 수 있는 최대 포도주양.j는 dp[i]가 몇번째 연속으로 마시는건지)

	dp[0][1] = wine[0]

	for i in range(1,N):
		dp[i][0] = max( dp[i-1][0].dp[i-1][[1],dp[i-1][2]) #현재 와인 안마심.다음은 무조건 마실 수 있음 
		dp[i][1] = max( dp[i-1][0] + wine[i], dp[i-1][1] )
		dp[i][2] = max( dp[i-1][1] + wine[i], dp[i-1][2] )

	return max( dp[N-1][0], dp[N-1][1], dp[N-1][2] )


	### bottom_up2#####
	#0X00, 0X0,X 세가지 중 하나 
	N = len(wine)
	dp = [0] * N
	dp[0] = wine[0]
	dp[1] = wine[0] + wine[1]
	
	for i in range(2,N):
	 dp[i] =max( dp[i-1],dp[i-2]+wine[i],dp[i-3] + wine[i-1]+wine[i]) 
	return dp[N-1]


if __name__ == "__main__":
	N = int(input())
	arr = [ int(input()) for _ in range(N) ]
	answer = solution(arr)

	print(answer)
