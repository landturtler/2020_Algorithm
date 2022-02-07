#경우의 수를 저장하는 배열 1개, visited배열을 참고해서 해당 위치까지의 최소시간 저장
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
visited = [-1]* (100001) #해당 위치까지 걸리는 최소 시간
cnt =  [-1] * (100001) #해당 위치까지 갈 수 있는 경우의 수 

cnt[N] = 1
visited[N] = 0
q = deque()
q.append([0,N])

while q:
	t,now = q.popleft()
	for x in ( now+1, now-1, 2*now):
		if 0 <= x < 100001:
			if visited[x] == -1: #한번도 도달한 적이 없으면 
				visited[x] = t+1
				cnt[x] = cnt[now]
				q.append([t+1,x])

			elif visited[x] == t+1: #직전에 도달한 적이 있으면 
				cnt[x] += cnt[now] #여기가 중요..!ㅎ

print(visited[K])
print(cnt[K])
