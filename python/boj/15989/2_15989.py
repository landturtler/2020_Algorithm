#15989 1,2,3 더하기 4
# 정수 N이 주어졌을 때, 1,2,3의 합으로 나타내는 방법의 수를 구하라
#dp[i][j]: 1,2,3을 오름차순으로만 더할 때, 마지막으로 더할 수가 j이면서 합이 i인 경우의 수 
#ex) dp[i][1] : 1로만 더해서 합이 i인 경우의 수, dp[i][2] : 1과 2로만 더해서 합이 i인 경우의 수 

MAX = 10001

if __name__ == "__main__": 
	answer = []
	dp = [[0,0,0,0] for _ in range(MAX)]
	dp[1][1] = 1 #1 
	dp[2][1] = 1 #1 1
	dp[2][2] = 1 # 2 
	dp[3][1] = 1 # 1 1 1 
	dp[3][2] = 1 # 1 2 
	dp[3][3] = 1 # 3

	for i in range(4,MAX):
		dp[i][1] = dp[i-1][1]# i-1에 1 더한 경우
		dp[i][2] = dp[i-2][1] + dp[i-2][2] # i-2에 2를 더한 경우
		dp[i][3] = dp[i-3][1] + dp[i-3][2]+ dp[i-3][3] #i-3에 3을 더한 경우 
		
	T = int(input())
	for _ in range(T):
		N = int(input())
		answer.append(sum(dp[N]))
	
	for x in answer:
		print(x)
