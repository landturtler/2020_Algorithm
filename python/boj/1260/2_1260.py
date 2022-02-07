
from collections import deque

def dfs(start):
	d_visited[start] = True
	print(start,end = " ")

	for nidx in range(N+1):
		if arr[start][nidx] == True and d_visited[nidx] == False:
			dfs(nidx)
	
def bfs(start):

	dq = deque()
	dq.append(start)
	b_visited[start] = True
	while dq:
		cx = dq.popleft()
		print(cx,end =" ")
		for nidx in range(N+1):
			if arr[cx][nidx] == True and b_visited[nidx] == False:
				dq.append(nidx)	
				b_visited[nidx] = True

if __name__ == "__main__":
	N,M,start = map(int,input().split())
	d_visited = [False] * (N+1)
	b_visited = [False] * (N+1)
	arr = [ [False]* (N+1) for _ in range(N+1) ]
	for _ in range(M):
		a,b = map(int,input().split())
		arr[a][b] = arr[b][a] = True

	#dfs 수행
	dfs(start)
	print("")
	#bfs 수행
	bfs(start)



