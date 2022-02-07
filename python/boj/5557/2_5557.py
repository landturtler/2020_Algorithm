#dp[i][j] : i번째 전까지의 계산값이 j일 때, j와 남은 수들의 연산으로 결과값을 만들 수 있는 경우의 수
#함수 호출 할 때, (0,0)이 아니라 (1,arr[0])으로 해야 함 -- 1번째 값이 0인 경우에 2번 세짐
#1차원 리스트 만들 때 [0] * N으로 하기 (N) 안됨
import sys
input = sys.stdin.readline

dp = []

def go(cnt,total,arr):
	global dp
	if dp[cnt][total] != 0:
		return dp[cnt][total]
	 	
	if cnt == N-1:
		if total == arr[N-1]:
			return 1
		else:
			return 0
	
	if total + arr[cnt] <= 20:
		dp[cnt][total] += go( cnt+1,total + arr[cnt],arr)

	if total - arr[cnt] >= 0:
		dp[cnt][total] += go( cnt+1,total - arr[cnt],arr)
	
	return dp[cnt][total]


if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	dp = [ [0]*(21) for _ in range(N) ]

	answer = go(1,arr[0],arr)
	print(answer)
