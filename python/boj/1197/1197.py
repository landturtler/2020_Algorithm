# 최소 스패닝 트리, MST
# 최소스패닝 트리는 어차피 순서가 없으므로 a,b = c랑 b,a = c를 굳이 따로 저장할 필요 없음

#특정 원소가 속한 집합 찾기
#union-by-rank: 각 트리에 대해 높이를 기억. 두 트리의 높이가 다르면 높이가 작은 트리를 큰 트리에 붙임(높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되도록 함)
parent = []

def find(x):
	global parent
	if parent[x] == x:
		return x
	parent[x] = find(parent[x])
	return parent[x]

#두 원소가 속한 집합을 합치기 (간선을 연결)
def union(a,b):
	global parent 
	roota = find(a)
	rootb = find(b)
	
	if roota < rootb:
		parent[rootb] = roota 
	elif roota > rootb:
		parent[roota] = rootb
	else:
		parent[roota] -= 1


#크루스칼 알고리즘 사용 	  
def solution(V,edges):
	answer = 0
	global parent 
	parent = [ i for i in range(V+1) ] #부모를 자기 자신으로 초기화 
	edges.sort() #비용순으로 오름차순 정렬

	#union 연산 수행
	for edge in edges:
		cost,a,b = edge
	#사이클이 발생하지 않는 경우--부모원소가 같지않은 경우-- 집합에 포함
	if find(a) != find(b):
		union(a,b)
		answer += cost
	
	return answer 


if __name__ == "__main__":
	V,E = map(int,input().split())
	edges = []

	for _ in range(E):
		a,b,c = map(int,input().split())
		edges.append( (c,a,b))
	
	answer = solution(V,edges)
	print(answer)


