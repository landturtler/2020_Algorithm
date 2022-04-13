'''
소요 시간 : 25분
문제 : 마을 개수 N, 배달 가능한 시간 K가 주어질 때 K시간 이내로 도달할 수 있는 마을 개수 리턴
알고리즘 : 최단경로(다익스트라)
배운 점 : 두 마을 a,b를 잇는 도로가 2개 이상이면 visited 사용하면 안됨
        arr2 = list(filter(lambda x : x<= K, arr1)) #arr1에서 K이하인 대상만 추출한 리스트
'''
import heapq
def solution(N, road, K):
    answer = list()
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)] * (N+1)
    
    # 1.그래프 만들기 
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    # 2.1번부터 탐색 시작
    hq = []
    heapq.heappush(hq,(1,0)) #도시, 거리
    distance[1] = 0
    
    while hq:
        cur,dis = heapq.heappop(hq)
        
        for i in range(len(graph[cur])):
            nex,cos = graph[cur][i][0], graph[cur][i][1]
            if dis + cos <= min(distance[nex],K): 
                distance[nex] = dis + cos
                heapq.heappush(hq,(nex,dis + cos))
                
    answer = list( i for i in range(len(distance)) if distance[i] <= K)
    
    return len(answer)
