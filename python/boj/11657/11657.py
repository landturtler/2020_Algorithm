#11657 타임머신
#N개 도시, M개의 버스가 있다. 버스 정보는 A->B 도시를 가는데 C만큼 걸린다. 이 때 C는 음수와 0이 가능하다.
# 1번도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하라
# 알고리즘 : 음수가 가능한 그래프 => 벨만포드 + 음수 사이클 탐지방법
# 실수했던 것 : ()는 tuple, {}는 dictionary, []는 array
import sys
input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
	N, M = map(int,input().split())
	bus = [] #모든 간선 정보 
	dist = [INF] * (N+1) #최단 거리 테이블 

	#A -> B까지 C의 비용이 든다. 
	for _ in range(M):
		a,b,c = map(int,input().split())
		bus.append((a,b,c))

	#벨만포드 알고리즘 
	def bell(start):
		dist[start] = 0 #시작노드는 항상 거리 0
		for i in range(N): #노드 
			for j in range(M): #간선 
				cur_n = bus[j][0] #현재 노드
				next_n = bus[j][1] #다음 노드
				cost = bus[j][2] #가중치
				#현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 update
				if dist[cur_n] != INF and dist[next_n] > dist[cur_n] + cost:
					dist[next_n] = dist[cur_n] + cost
					#N-1번 이후 반복에도 값이 갱신되는 경우, 음수 loop
					if i == N-1:
						return True
		return False
	
	#벨만포드 수행
	is_negative_cycle = bell(1)
	if is_negative_cycle:
		print('-1') 
	else:
		#1번 노드를 제외한 다른 모든 노드로 가기위한 최단 거리
		for i in range(2,N+1):
			if dist[i] == INF:
				print('-1')
			else:
				print(dist[i])
			




