#프림 알고리즘
#프림 알고리즘은 a -> b값이 주어지면  b->a값도 넣어야 함

import heapq  #프림 
import sys
from collections import defaultdict #빈 리스트를 생성 


def solution(V,edges):
	mst = list() #최소신장트리
	visited = [False] * (V+1) #방문 확인 리스트
	answer = 0
#1번 노드부터 탐색시작
	visited[1] = True
	hq = edges[1] 
	heapq.heapify(hq) #1번 노드에 연결된 정보를 우선순위 큐로 바꿈

	while hq:
		cost,a,b = heapq.heappop(hq)
		#방문한 적이 없는 노드면 mst에 추가 
		if visited[b] == False:
			visited[b] = True
			mst.append( (a,b) )
			answer += cost
		#방금 추가한 노드의 간선 정보 추가 
			for edge in edges[b]:
				if visited[edge[2]] == False:
					heapq.heappush(hq,edge)
	return answer

if __name__ == "__main__":
	V,E = map(int,input().split())
	edges = defaultdict(list) #빈 그래프 생성 
	for _ in range(E):
		a,b,c = map(int,input().split())
		edges[a].append( [c,a,b] )
		edges[b].append( [c,a,b] )
	
	answer = solution(V,edges)
	print(answer)

