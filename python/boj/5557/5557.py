# 5557 1학년
# 수 사이에 덧셈,뺄셈을 붙여서 연산 결과값이 마지막 숫자와 동일한 수식을 만들고 싶다. 중간에 나오는 수가 20 이하, 0이상이어야 한다. 
# 숫자가 주어졌을 때 상근이가만들 수 있는 올바른 등식의 수를 구하라 
#리스트로 입력받을 때 왜 어쩔 땐 [] 되고 어쩔땐 []가 안되지 
import sys
input = sys.stdin.readline
dp = []

def solution(N,arr):
	dp = [ [0]*21 for _ in range(N) ] #dp[i][j] : i번째 숫자까지 봤을 때 값이 j가 되는 경우의 수 
	print(dp)
	dp[0][arr[0]] = 1

	for i in range(1,N-1): #맨 마지막 숫자는 연산하지 안흥ㅁ 
		num = arr[i]
		
		for j in range(21):
			if dp[i-1][j] == 0:
				continue

			if (j + num) <= 20:
				dp[i][j+num] += dp[i-1][j] 
			
			if (j - num) >= 0:
				dp[i][j-num] += dp[i-1][j] 
		
	
	return dp[N-2][arr[N-1]]
		
		

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split(" ")) )

	answer = solution(N,arr)
	print(answer)
