#2252 줄 세우기 ( 위상정렬 )
# 위상정렬 특징 : 단방향 간선이 존재. disjoint-set이랑 헷갈리지 말것. union-find기반 알고리즘은 순서가 필요 X
# 위상정렬은 visited,단방향 그래프, 진입 차수 리스트 가 필요함 
#보통 그래프에선 자료구조를  연결리스트(2차원 리스트) 혹은 dictionary로 함. 음.... 연결 리스트로 하장 
#from collections import defaultdict 한 후에 arr= defaultdict(list)
#2차원 배열 입력받을 때 arr.append( [ map(int,input().split())]) 말고 arr.append( list(map(int,input())) )으로 해야 한다...

'''
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 반복
	- 원소를 꺼내 해당 노드에서 출발하는 간선을 제거
	- 새롭게 진입차수가 0이 된 노드를 큐에 삽입
3. 만약 모든 노드를 방문하기 전 큐가 닫히면 사이클인거임
(근데 보통 위상정렬은 사이클 발생 안하도록 제시함)
'''

from collections import deque, defaultdict 

def solution(N,arr):
	answer = []
	graph = defaultdict(list)
	indegree = [0] * (N+1)

	#위상정렬 그래프 생성 
	for ar in arr:
		a,b = ar
		graph[a].append(b) #리스트 이므로 [a] = b가 아니라 append
		
		indegree[b] += 1
	
	#위상정렬 수행
	q = deque()
	
	#진입차수가 0인 노드들 큐에 삽입
	for i in range(1, N+1):
		if indegree[i] == 0:
			q.append(i)
	
	while q:
		cur = q.popleft()
		answer.append(cur)
		# 해당 원소와 연결된 노드 진입차수들 -1하기 
		for i in graph[cur]:
			indegree[i] -= 1

		# 새롭게 진입 차수가 0 되는 노드를 큐에 삽입 
			if indegree[i] == 0:
				q.append(i)
			
	return answer


if __name__ == "__main__":
	N,M = map(int,input().split())
	arr = list()
	for _ in range(M):
		arr.append( list(map(int,input().split())))

	answer = solution(N,arr)
	for x in answer:
		print(x,end = " ")
