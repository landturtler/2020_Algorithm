'''
Programmers LV3
알고리즘 : BFS
고려해야 하는 것 : 로봇 길이가 2이기 때문에 좌표 저장 시 두 쌍의 좌표로 넣어야 함. 
처음 풀 때 백준 파이프 옮기기 문제랑 비슷하다 생각해서 좌표를 하나만 넣어도 된다고 생각했는데, 왜 하나만 넣으면 안되는지에 대해 좀 더 고민해 볼 것
+ 지난번 풀었던 경주로 건설과 차이점 생각해보기
처음 안 것 : 이동하는 로봇의 길이가 2인 경우는 visited배열을 만들 때 list()를 미리 만들어 두지 말고, 빈 리스트 생성해서 방문 할 때마다 (x1,y1,x2,y2)로 삽입하는 방법도 있다..!
        범위 벗어나는거 자꾸 체크하기 귀찮으면 그냥 맨 바깥에 벽을 하나 더 만들기
풀이 시간 : 아직 미해결
'''

from collections import deque

def solution(board):
    
    N = len(board)
    board = [[1] + b + [1] for b in board]
    board = [[1] * (N + 2)] + board + [[1] * (N + 2)]
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    
    q = deque()
    visited = []
    
    q.append([0,0,0,1,0])# 로봇 좌표, cost
    visited.append(((0,0),(0,1)))
    
    while q :
        cx1,cy1,cx2,cy2, cost = q.popleft()

        if (cx1 == N and cy1 == N) or (cx2 == N and cy2 == N) :
            answer = cost
            break

        #상하좌우 이동
        for k in range(4) :
            nx1 = cx1 + dir[k][0]
            ny1 = cy1 + dir[k][1]
            nx2 = cx2 + dir[k][0]
            ny2 = cy2 + dir[k][1]
                      
            if board[nx1][ny1] == 0 or board[nx2][ny2] == 0:
                continue
            
            if ((nx1,ny1),(nx2,ny2)) not in visited:
                visited.append(((nx1,ny1),(nx2,ny2)))
                q.append([nx1,ny1,nx2,ny2,cost+1])
                
        # 대각선 이동 
        if cx1 == cx2:
            for i in [-1, 1] : # 위 / 아래 
                if board[cx1+i][ny1] == 0 and board[cx2+i][cy2] == 0:
                    if ((cx1+i,cy1),(cx2,cy2)) not in visited:
                        visited.append(((cx1+i,cy1),(cx2,cy2)))
                        q.append([cx1+i,cy1,cx2,cy2,cost+1])
                        
                    if ((cx1,cy1),(cx2+i,cy2)) not in visited:
                        visited.append(((cx1,cy1),(cx2+i,cy2)))
                        q.append([cx1,cy1,cx2+i,cy2,cost+1])

        elif cy1 == cy2 :
            for i in [-1, 1] : # 왼 / 오
                if board[cx1][cy1+i] == 0 and board[cx2][cy2+i] == 0:
                    if ((cx1,cy1+i),(cx2,cy2)) not in visited:
                        visited.append(((cx1,cy1+i),(cx2,cy2)))
                        q.append([cx1,cy1+i,cx2,cy2,cost+1])  
                    if ((cx1,cy1),(cx2,cy2+i)) not in visited:
                        visited.append(((cx1+i,cy1),(cx2,cy2+i)))
                        q.append([cx1,cy1,cx2,cy2+i,cost+1])
                    
    return answer
