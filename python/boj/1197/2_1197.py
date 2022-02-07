#프림 알고리즘
#프림 알고리즘은 a -> b값이 주어지면  b->a값도 넣어야 함

import heapq  #프림 
import sys
from collections import defaultdict #빈 리스트를 생성 

V = 0

def solution(V,edges):
	answer = 0
	visited = [False] * (V+1)
	mst = [] #최소 힙 
	weights = [ sys.maxsize for _ in range(V+1) ] #최소 신장 트리 가중치 

#1번 노드부터 방문 시작.
	visited[1] = True
	hq = edges[1] #첫번째 노드와 연결된 간선 추출
	heapq.heapify(hq) #첫번째 노드와 연결된 간선 정보를 우선순위 큐로 생성
	mst = []

	while hq:
		cost,a,b = heapq.heappop(hq)
		#방문하지 않은 노드 발견 시 mst에 삽입 후 인접 간선 다시 찾기 
		if visited[a] == False:
			visited[a] = True
			mst.append( (a,b) )
			answer += cost

		#방금 넣은 노드의 인접 노드도 방문한 적이 없으면 해당 간선 정보 넣기 
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

