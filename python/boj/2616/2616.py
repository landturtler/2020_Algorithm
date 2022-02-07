#2616 소형기관차
# 1~N번 객차에 손님 수가 주어진다. 소형 기관차는 3대가 있고, 각 기관차가 최대로 데려갈 수 있는 객차 수가 주어진다. 3대의 소형 기관차를 이용하여 최대로 운송할 수 있는 손님 수는?
#dp[i][j]: i번째 객차까지 탐색하고, j개의 소형 기관차를 사용하였을 때 운송할 수 있는 최대 손님 수 


import sys
input = sys.stdin.readline

def solution(N,K,arr):
	dp = [ [0]*4 for _ in range(N)] 
	dp[K-1][1] = sum(arr[0:K]) #0~K번째 객차를 처음 선택했을 경우

	for i in range(K,N):
		dp[i][1] = max(dp[i-1][1], sum(arr[i-K+1:i+1]))
		dp[i][2] = max(dp[i-1][2], dp[i-K][1] + sum(arr[i-K+1:i+1]))
		dp[i][3] = max(dp[i-1][3], dp[i-K][2] + sum(arr[i-K+1:i+1]))
	
	return dp[N-1][3]

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	K = int(input())
	
	answer = solution(N,K,arr)
	print(answer)
