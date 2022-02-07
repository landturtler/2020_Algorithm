#bfs로 풀기
import sys
from collections import deque
from itertools import permutations
INF = sys.maxsize

def solution(N,scv):
	q = deque()
	cur = [ scv[0],scv[1],scv[2],0]
	q.append(cur)
	perm = list(permutations([1,3,9],3))
	answer = 0
	dp = list(list([INF] * 61 for _ in range(61)) for _ in range(61))

	while q:
		cur = q.popleft()
		if cur[0] == 0 and cur[1] == 0 and cur[2] == 0:
			answer = cur[3]
			break

		else:
			for pe in perm:
				nex=[max(cur[0] - pe[0],0),max(cur[1]-pe[1],0),max(cur[2]-pe[2],0), cur[3] + 1]
				if dp[nex[0]][nex[1]][nex[2]] != INF:
					continue
				dp[nex[0]][nex[1]][nex[2]] = nex[3]
				q.append(nex)
	return answer

if __name__ == "__main__":
	N = int(input())
	scv = [0,0,0]
	tmp = list(map(int,input().split()))
	for i in range(len(tmp)):
		scv[i] = tmp[i]	
	answer = solution(N,scv)
	print(answer)

