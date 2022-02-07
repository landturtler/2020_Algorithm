#12869 뮤탈리스크
# N개의 SCV가 있고, 각 SCV는 체력이 있다.뮤탈리스크는 한번에 서로 다른 3개의 SCV를 공격할 수 있으며 순서대로 (9,3,1)만큼 공격할 수 있다. 모든 SCV를 파괴하기 위해 공격해야 하는 공격횟수의 최솟값을 리턴해라
#dp배열의 인덱스값 정의후보와 값..,, i번 수행했을 때 남은 각 값들의 최솟값? 
# N <= 3이고, 각 SCV 체력이 60이하이므로, 그래서 N개의 SCV체력을 각각 메모모이제이션할 수 있다 
#dp[i][j][k] : scv체력이 각각 i,j,k일 때 앞으로 필요한 최소공격횟수 
# 최솟값 구하는 방법 : dp[i][j][k] = min (dp[i][j][k], go(i-9,j-3,k-1) + 1)
# 생각 흐름: 브루트 포스로 생각,. 3개 SCV가 다 0이 될 때까지 answer = min(answer, solution(t[0],t[1],t[2]) + 1)로 탐색.
# 그 후에 뭘 메모이제이션 할까..하고 보니 함수의 인자로 건넸던 각 scv값들을 dp로 넣으면 되겠구나~! 

import sys
from itertools import permutations
input = sys.stdin.readline
MAX = 61
INF = sys.maxsize

comb = list(permutations([1,3,9],3))
dp = list( list( [INF]*MAX for _ in range(MAX)) for _ in range(MAX) )# dp[i][j][k] : 각 체력이 i,j,k일때 앞으로 필요한 최소 공격 횟수... 그러면 dp[0][0][0] 값이 내가 원한 값 
		
def solution(a,b,c):
	a = max(a,0)
	b = max(b,0)
	c = max(c,0)
	if a == 0 and b == 0 and c == 0:
		return 0
	
	elif dp[a][b][c] != INF:
		return dp[a][b][c]

	else:
		global comb
		for co in comb:
			dp[a][b][c] = min(dp[a][b][c],solution(a-co[0],b-co[1],c-co[2])+1)
		return dp[a][b][c]
		

if __name__ == "__main__":
	N = int(input())
	scv = [0,0,0]
	arr = list(map(int,input().split()))
	for i in range(len(arr)):
		scv[i] = arr[i]
	answer = solution(scv[0],scv[1],scv[2])
	print(answer)
	

