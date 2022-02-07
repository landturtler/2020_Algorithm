#12951 숨바꼭질 2
# 수빈이 위치가 X이면 X-1, X+1, 2*X만큼 이동할 수 있다.
#수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지,그 방법은 몇가지인지?
#dp 배열에 담을 수 있는지가 의문 
# 처음에 최소시간이니까 bfs로 풀려했음. 그런데 3초에 K에 도달했다고 pop했을 때, 큐에 2초짜리이면서 K에 도달하기 직전 값들이 있을거라 생각했기 때문.그럼 이 경우의 수는 count하지 못할거라 생각했다.
#그렇지만 이건 오해. 왜냐면 BFS는 너비탐색이므로 큐에는 항상 3초 이후의 자료들이 저장되어있다. 예를들어 3초 데이터를 탐색하기 위해선 2초 데이터를 다 탐색하고 나야 3초껄 pop할 수 있으므로..
# BFS에선 visited도 쓸 수 있다. 왜냐하면 맨 처음 해당 지점에 도달했다는 건,최소 시간으로 도달했다는 의미이므로 그 이후에 다시 특정 지점에 오는건 의미가 없다.
# 반대로 DFS는 visited 쓰면 안된다. 맨 첨 특정 지점에 도착한 시간이 최소시간이라는 보장이 엇기 때문 
# 중복 개수를 확인해야 한다는데 모르겟따.

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
visited = [-1] * (100001)
answer = [0,0] #걸린 시간, 경우의 수 
q = deque()
q.append([0,N]) #걸린 시간, 좌표

visited[N] = 0

while q:
	t,loc = q.popleft()
	print("popleft : t = ", t,", loc = ",loc);
	if loc == K:
		answer = [t,1]
		break
	else:
		if loc < 100001 and (visited[loc + 1] == -1 or visited[loc+1] == t+1):
			print("q.append",t+1,", ",loc+1)
			q.append([t+1,loc+1])
			visited[loc+1] = t + 1
		if loc > 0 and loc <= 100001 and (visited[loc - 1] == -1 or visited[loc-1] == t+1):
			q.append([t+1,loc-1])
			visited[loc-1] = t + 1
			print("q.append",t+1,", ",loc-1)

		if 2*loc <= K and (visited[loc*2] == -1 or visited[loc*2] == t +1):
			q.append([t+1,2*loc])
			visited[loc*2] = t + 1
			print("q.append",t+1,", ",loc*2)

#경우의 수 구하기
while q:
	t,loc == q.popleft()
	print("popleft2 : ",t,", ",loc)
	if t == answer[0] and loc == K:
		answer[1] += 1
		
print(answer[0])
print(answer[1])
