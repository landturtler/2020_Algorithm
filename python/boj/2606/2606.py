#2606 바이러스

MAX = 101
visited = [False] * MAX
answer = 0

def go(node,network):
	global visited,answer
	visited[node] = True

	for nx in range(N+1):
		if network[node][nx] == True and visited[nx] == False:
			go(nx,network)
			answer += 1		

def solution(N,arr):
	network = [ [False]*(N+1) for _ in range(N+1)]

	for x in arr:
		a,b = x[0],x[1]
		network[a][b] = network[b][a] = True

	go(1,network)

if __name__ == "__main__":
	N = int(input())
	V = int(input())
	arr = [ list(map(int,input().split())) for _ in range(V) ]
	solution(N,arr)
	print(answer)

