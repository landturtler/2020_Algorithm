'''
가장 먼 노드
풀이 시간 : 20분
알고리즘 : BFS
'''
from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    #1. 그래프, 거리 리스트 생성 
    distance = [int(1e9)] * (n+1) #1에서 n+1까지의 거리
    graph = defaultdict(list) #노드 간 연결관계, 그래프 
    for i in range(len(edge)):
        a,b = edge[i][0], edge[i][1]
        graph[a].append(b)
        graph[b].append(a)
    
    #2. BFS 큐 생성 및 탐색 
    q = deque()
    q.append((1,0))
    distance[1] = 0 
    
    while q:
        tmp = q.popleft()
        cur, dis = tmp[0], tmp[1]
        
        #현재 노드와 연결된 노드 중, 최단 거리 존재 시 update 
        for x in range(len(graph[cur])):
            nex = graph[cur][x]
            if dis + 1 < distance[nex]:
                distance[nex] = dis + 1
                q.append((nex,dis+1))
                
    #3. distance중 가장 먼 노드 개수 탐색 
    max_val = max(distance[1:])
    answer = distance.count(max_val)
    return answer
