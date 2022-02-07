#dfs 배열 말고 딕셔너리로 풀기
#2606 바이러스

MAX = 101
visited = [False] * MAX
answer = 0

def go(node,network):
	global visited,answer
	visited[node] = True
	for nx in network[node]:
		if visited[nx] == False:
			go(nx,network)
			answer += 1

def solution(N,arr):
	network = {}
	for x in arr:
		a,b = x[0],x[1]
		network[a].add(b)
		network[b].add(a)
	 
	go(1,network)

if __name__ == "__main__":
	N = int(input())
	V = int(input())
	arr = [ list(map(int,input().split())) for _ in range(V) ]
	solution(N,arr)
	print(answer)
