'''
문제 ; (0,0) -> (N-1,N-1)로 가는 경주로를 건설할 때 최소 비용은? (직선 비용 : 100원 / 코너비용 : 500원)
알고리즘 : BFS + DP
배운 점: 특정 방향으로 갈 때 비용이 다른 경우, visited[] 배열에 특정 방향을 고려해서 3차원으로 저장할 것
소요 시간 : 50분
'''

from collections import deque
INF = int(1e9)

def solution(board):
    answer = INF
    N = len(board)
    dir = [ [-1,0], [0,1], [1,0], [0,-1]] 
   #visited[i][j][0] : (i,j)에 수평방향으로 도달할 수있는 최소 비용  / visited[i][j][1] : (i,j)에 수직 방향으로 도달할 수 있는 최소 비용 
    visited = [[[INF] *2 for _ in range(N)] for _ in range(N)]  
    q = deque()
    
    q.append([0,0,0,1]) #(x,y)좌표 / 건설 비용 / 직전 방향(우측으로 이동) 
    q.append([0,0,0,2]) #(x,y)좌표 / 건설 비용 / 직전 방향(아래로 이동) 
    visited[0][0][0] = 0
    visited[0][0][1] = 0
    
    while q:
        cx,cy,cc,cd = q.popleft()
        # (N-1,N-1)에 도달한 경우, 최소 건설 비용 계산
        if cx == N-1 and cy == N-1:
            answer = min(answer,cc)
            continue
            
        #현재 위치까지의 건설 비용이 (N-1,N-1)까지 가는 최소 비용보다 큰 경우 탐색 중단
        if answer < cc:
            continue
        
        for k in range(4):
            nx = cx + dir[k][0]
            ny = cy + dir[k][1]
            nc = 0
            if ((cd % 2) == (k % 2)):
                nc = cc + 100
            else:
                nc = cc + 600
            nd = k
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1 or visited[nx][ny][nd%2]  < nc:
                continue
                
            q.append([nx,ny,nc,nd])
            visited[nx][ny][nd%2] = nc
    return answer
