#1916 최소비용 구하기 
#N개 도시가 주어지고, 각 도시로 이동하는 M개 버스가 있다. A->B로 가는데 드는 최소한의 버스 비용을 출력하라
#특정 노드 -> 다른 노드 최단 거리 : 다익스트라. 모든 거리 : 플로이드 워셜(N^3)
#우선순위 큐는 heapq이고 그냥 큐는 deque사용..! 헷갈리지 말자 
#우선순위 큐는 deque() 하는게 아니라 []로 선언 후에 heqppush(q,값)으로 삽입하는 거임ㅠㅜ 
# 최단거리에서 필요한 것 ; 간선 정보 리스트, visited, 최단거리 리스트
#INF = int(le9)
#최단거리 구할땐 중간에 큐의 pop한게 도착노드라도 break하지 않음

from heapq import heappush, heappop
INF = 100000001

def dijkstra(bus,start,end):
	hq = []
	distance = [INF] * (N+1)

	#시작노드를 큐에 삽입하고 최단 경로 구하기
	heappush(hq,(0,start)) #비용, 시작 노드
	distance[start] = 0

	while hq:
		dist,cur_node = heappop(hq)
	#이미 그 노드로 가는 최단경로를 구한 적이 있고, 그 거리가 큐에서 뽑은 거리보다 작은 경우 pass
		if distance[cur_node] < dist:
			continue
	# 아직 최단 경로를 구한 적이 없거나, 예전에 거리를 구했어도 지금 큐에서 뽑은 거리가 더 작은 경우. 인접 노드에 연결된 최단 거리도 update 
		else:
			if cur_node in bus:
				for adj_node in bus[cur_node]:
					cost = dist + adj_node[1]
					if cost < distance[adj_node[0]]:
						distance[adj_node[0]] = cost
						heappush(hq,(cost,adj_node[0]) )
	
	return distance[end]

if __name__ == "__main__":
	N = int(input())
	M = int(input())
	bus = {}
	#간선 정보 입력받기 
	for _ in range(M):
		a,b,c = map(int,input().split())
		
		if a not in bus:
			bus[a] = []
		bus[a].append( (b,c) )	
	
	start, end = map(int,input().split())

	answer = dijkstra(bus,start,end)
	print(answer)
