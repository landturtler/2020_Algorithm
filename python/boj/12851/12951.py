#12951 숨바꼭질 2
# 수빈이 위치가 X이면 X-1, X+1, 2*X만큼 이동할 수 있다.
#수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지,그 방법은 몇가지인지?
#dp 배열에 담을 수 있는지가 의문 
# 처음에 최소시간이니까 bfs로 풀려했는데

import sys
from collections import deque
input = sys.stdin.readline
MAX = sys.maxsize

N,K = map(int,input().split())
answer = [MAX,0] #걸린 시간, 경우의 수 

def go(direct,tim):
	global answer
	#print("dir = ",direct,",tim = ",tim)
	if tim > answer[0]:
		return
	if direct == K:
		#print("tim = ",tim)
		if answer[0] > tim:
			answer = [tim,1]
		elif answer[0] == tim:
			answer[1] += 1
	else:
		go(direct+1,tim+1)
		go(direct-1,tim+1)
		go(2*direct,tim+1)

go(N,0)
print(answer[0])
print(answer[1])

