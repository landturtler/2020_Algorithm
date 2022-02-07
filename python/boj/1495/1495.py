#1495 기타리스트
#N개의 곡을 연주하고, 각 곡마다 볼륨을 바꾸고 연주하려 한다. 볼륨 리스트가 V라 하고, 현재 볼륨이 P라 하면,i번째 곡은 P + V[i] 혹은 P - V[i]로 연주해야 한다. 각 볼륨은 0이상, M이하여야 할 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값은?
# dp[i][j] : i번째 곡까지 연주했을 때, 최댓값(j = 0은 V[i]를 더함. j = 1은 V[i]를 뺌)

#input = sys.stdin.readline할 때 strip()도 쓰면 마지막값이 입력 안될 수 있음! 그냥 readline까지만 쓰기 
#처음에 dp[idx]로만 했는데, 중간에 최댓값이 끝까지 최댓값이 되는건 아님..이건 고려했던 상황 -> 이것처럼 중간의 최댓값이 항상 결과값도 최대를 보장하는게 아니라면 2차원 배열 고려해보기 dp[i][j] : i~j까지의 최댓값. 혹은 dp[i][2] : dp[i][0]은 i번째 곡 전에 V[i]를 빼었을 때 최댓값
#2차원 배열 선언 방법 : [-1,-1] * M 하면 1차원 배열됨 // list([-1,-1] for _ in range(N)) 해야 함

import sys
input = sys.stdin.readline
MAX = 10001

if __name__ == "__main__":
	N,S,M = map(int,input().split())
	dp = list( [-1,-1] for _ in range(MAX) )
	V = list(map(int,input().split()))
	dp[0] = [S,S]
	V.insert(0,S)

	for i in range(1,N+1):
		cmp1 = dp[i-1][0] + V[i]
		cmp2 = dp[i-1][1] + V[i]
		cmp3 = dp[i-1][0] - V[i]
		cmp4 = dp[i-1][1] - V[i]
		
		if cmp1 > M:	cmp1 = -1
		if cmp2 > M:	cmp2 = -1
		if cmp3 < 0:	cmp3 = -1
		if cmp4 < 0:	cmp4 = -1

		dp[i][0] = max(cmp1,cmp2)
		dp[i][1] = max(cmp3,cmp4)
	answer = max(dp[N])
	print(answer)
