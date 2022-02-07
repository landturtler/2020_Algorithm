
# M좌표부터 달리기 시작.a
#오래걸린 것: 만약 이동후에 새로운 가장 큰 값을 한번에 구하려면 어떻게 해야 하는지? 
#슬라이딩 윈도우 : 처음과 끝에 삽입삭제가 빈번하게 이뤄지기 떄문에 보통 Deque를 자주 사용한다. 최댓값과 최솟값을 구하려면 우선순위큐를 사용해도 된다.

from heapq import heappush, heappop

N,M = map(int,input().split())
arr = list(map(int,input().split()))
hq = []
answer = []

#0 ~ 2*M-2까지의 값 삽입
for i in range(0,2*M-1):
	heappush(hq,tuple(-arr[i],i))

answer.append( -(hq[0][0]))

#한 칸씩 움직이면서 max값 확인
for idx in range(2*M-1,N):
	heappush(hq,tuple(-arr[idx],idx))
	while hq[0][1] < (idx - (2*M-1)):
		heappop(hq)
	answer.append( -(hq[0][0]) )

print(answer)
	


