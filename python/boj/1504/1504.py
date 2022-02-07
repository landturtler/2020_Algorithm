#특정한 최단 경로 : 다익스트라, 1->v1->v2->end, 1->v2->v1->end
#우선순위 큐 사용 
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#입력받기
N,E = map(int,input().split()) #노드개수,간선개수
graph = [[] for _ in range(N+1)] #각 노드에 연결되어 있는 노드 정보 리스트
         
#모든 간선 정보 입력받기
for _ in range(E):
	a,b,c = map(int,input().split()) #a -> b노드로 갈 때 c 비용
	graph[a].append((b,c))
	graph[b].append((a,c))

v1, v2 = map(int, input().split())    
          
def dijkstra(start):
	q = []   # (해당 노드까지 최단경로,노드) 입력 
	distance = [INF] * (N+1) #최단 거리 테이블
          
  #시작노드를 큐에 삽입
	heapq.heappush(q,(0,start))
	distance[start] = 0
	while q: 

    #가장 최단 거리가 짧은 노드 정보 가져오기
		dist, cur_node = heapq.heappop(q)
    # 이미 그 노드로 가는 최단 경로를 구한 적 있고, 그 거리가 큐에서 뽑은 거리보다 작은 경우 
		if distance[cur_node] < dist:
			continue
      
	# 아직 최단 경로를 구한 적 없거나, 에전에 거리를 구했어도 지금 큐에서 뽑은 거리가 더 작은 경우 
		else:
			for adj_node in graph[cur_node]: #해당 노드에 연결된 인접 노드 확인. adj_node[0] : 인접 노드 번호, adj_node[1] : cur_node - 인접 노드 까지의 거리  
				cost = dist + adj_node[1]  
				if cost < distance[adj_node[0]]:
					distance[adj_node[0]] = cost 
					heapq.heappush(q, (cost, adj_node[0]))
	return distance


# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
ori_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

path_1 = ori_distance[v1] + v1_distance[v2] + v2_distance[N]
path_2 = ori_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(path_1, path_2)
print(result if result < INF else -1)
