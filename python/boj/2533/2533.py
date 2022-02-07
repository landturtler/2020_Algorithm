#2533 
# 친구 관계 트리가 주어졌을 때 모든 개인이 새로운 아이디어를 수용하기 위해 필요한 최소 노드 개수 
'''
dp[i][0]: i번째 노드가 얼리어답터인 경우, 본인 + 자식 노드 중 문제 조건을 만족하는 최소 얼리어답터?
dp[i][1] : i번째 노드가 일반일 경우, 문제 조건을 만족하는 최소 얼리어답터
'''
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
graph = [ [] for _ in range(N+1)] #양방향 그래프 
dp = [ [INF,INF] for _ in range(N+1) ] #[정점번호][얼리어답터 체크]
visited = [False] * (N+1)

#그래프 입력 
for _ in range(N-1):
	u, v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u) 

def solution(num,idx):
	if dp[num][idx] != INF:
		return dp[num][idx]
	else:		
		dp[num][0] = 1 #내가 얼리어답터일때
		dp[num][1] = 0 #내가 일반인일때

		for i in graph[num]:
			if visited[i] == True:
				continue
			visited[i] = True
			cmp1 = solution(i,0)
			cmp2 = solution(i,1)
			dp[num][0] += min(cmp1,cmp2) #내가 얼리어답터면 친구가 얼리어답터일경우,아닐경우 둘 중 작은값을 더함 (어차피 내가 얼리어답터이므로 상관없음)
			dp[num][1] += cmp1 #내가 일반인이면 친구가 얼리어답터야 함
		return dp[num][idx]

visited[1] = True
print( min(solution(1,0),solution(1,1)) )
			

