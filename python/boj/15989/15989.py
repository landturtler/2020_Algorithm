#15989 1,2,3 더하기 4
# 정수 N이 주어졌을 때, 1,2,3의 합으로 나타내는 방법의 수를 구하라
#dp[i] : 정수 i를 1,2,3의 합으로 나타내는 방법의 수. 단 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.
#dp [i] = dp[i-1] + dp[i-2] + dp[i-3]
import sys
INF = sys.maxsize
MAX = 10001

if __name__ == "__main__": 
	answer = []
	dp = [1]* MAX
	
	for i in range(2,MAX):
		dp[i] += dp[i-2]
	
	for i in range(3,MAX):
		dp[i] += dp[i-3]
	
	T = int(input())
	for _ in range(T):
		N = int(input())
		answer.append(dp[N])
	
	for x in answer:
		print(x)

	
