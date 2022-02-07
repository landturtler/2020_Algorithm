#2281 데스노트
# 노트에 정해진 순서대로 N명의 이름을 적으려 한다. 이름 사이엔 빈 공간 한 칸을 두고, 각 줄의 끝에 사용하지 않고 남게되는 칸 수 제곱의 합이 최소가 되려 한다.(단 맨 마지막 줄 제외) 제곱합의 최소값은?
# 경우의 수 구하는 거면 += 1 하는 방식이거나 += (이전 dp값)
# 최소값을 구하는 거면 min( , () + 1) 등의 방식으로 구하기 
#dp[i][j] : i번째이름을 썼을때 남은 칸수 제곱의 합. j를 처음엔 칸수로 했는데, 열의 번호를 모르면 어느 값까지를 제곱하고 합해야 하는지 모름
# 즉, 사람 번호, 열 위치, 칸 위치를 모두 알아야 한다고 생각했음
# -> 3차원은 아닌것같음.. 셋 중에 칸 위치는 몰라도 됨! 
# dp[i][k] : i번째 글자를 넣으려 할 때, 현재 줄에서 남은 빈칸 수가 k일때 지금까지 빈칸 제곱의 합..! 
# MAX값을 무턱대고 maxsize로 하면 안됨 
# 난 처음에 뺄 떄 -1을 같이 계속 뻈는데, 그렇게 되면 안됨..,, 
# 재귀가 대얄 1000번 될것 같으면 재귀 조건 풀어야 함!!
import sys
input = sys.stdin.readline
MAX = sys.maxsize

dp = [] 
def go(num,rem):
	global dp
	if num >= N:
		return 0
	
	elif dp[num][rem] != MAX:
		return dp[num][rem]
	
	else:
	 	#다음 줄에 작성하기
		next_rem = M - arr[num]
		dp[num][rem] = rem * rem + go((num + 1), next_rem)
		
		#현재 줄에 작성할 수 있는 경우, 최솟값 찾기
		if arr[num] < rem and rem > 0:
			next_rem = rem - arr[num] - 1
			dp[num][rem] = min(dp[num][rem], go((num + 1), next_rem))
	return dp[num][rem]

if __name__ == "__main__":
	N, M = map(int,input().split())
	arr = list( int(input()) for _ in range(N) )
	dp = list( [MAX] * (M+1) for _ in range(N) )
	
	answer = go(1, M - arr[0])
	print(answer)
