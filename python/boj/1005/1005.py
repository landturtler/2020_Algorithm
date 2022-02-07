#위상정렬: visited, 단방향 그래프, 진입차수리스트, 큐가 필요하다!!1
#노드나 그래프 번호가 있는 문제는 0~N말고 0~N+1까지 정의하자!!
# 이번 위상정렬에선 "visited쓰지 말고 dp배열에 최댓값들을 저장해야 한다. .! why
from sys import stdin
from collections import deque,defaultdict
input = stdin.readline

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		N, K = map(int,input().split())
		answer = 0
		building = [0]
		building.extend( list(map(int,input().split())))#건물의 건설시간 
		indegree = [0] * (N+1)
		visited = [False] * (N+1)
		dp = [ -1 for _ in range(N+1)] #해당 건물까지 걸리는 시간 
		order = defaultdict(list)

		#건물 별 인접관계 정보 저장
		for _ in range(K):
			a,b = map(int,input().split())
			order[a].append(b)	
			indegree[b] += 1

		#마지막 건물 번호 저장
		W = int(input())
		
		#진입 차수가 0인 빌딩 삽입
		q = deque()
		for i in range(1,N+1):
			if indegree[i] == 0:
				q.append(i)
				dp[i] = building[i]

		while q:
			cur = q.popleft()
			
			for x in order[cur]:
					indegree[x] -= 1 #진입차수 줄이고 비용 갱신 
					dp[x] = max( dp[x], dp[cur] + building[x] ) # 기존의 최댓값과 이번에 지을 건물의 비용 중 큰 값 선택 

					if indegree[x] == 0:
						q.append(x)

		print(dp[W])

		
