#dp로 풀기
#dp[N] = N일까지 일할 때 벌 수 있는 최대 금액 

N = int(input())
dp = [0] * N 
arr = [ list(map(int, input().split())) for _ in range(N) ]

#상담 비용은 상담이 끝난 다음날부터 더함 
for start_day in range(N):
	for next_day in range(start_day + arr[next_day][0])
	

