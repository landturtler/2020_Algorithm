#dp[i] :i번째a 음악까지 연주할때 가능한 볼륨의 개수를 딕셔너리로 저장
#set은 add로 추가,discard로 삭제

import sys
from collections import defaultdict
input = sys.stdin.readline
MAX = 101

if __name__ == "__main__":
	N,S,M = map(int,input().split())
	V = list(map(int,input().split()))
	V.insert(0,S)
	dp = [ set([-1]) for _ in range(MAX) ]
	dp[0].add(S)

	for i in range(1,N+1):
		for x in dp[i-1]:
			if x == -1:
				continue

			if x + V[i] <= M:
				dp[i].add(x + V[i])
			if x - V[i] >= 0:
				dp[i].add(x - V[i])
	print(max(dp[N]))

			
	
