'''
Programmers LV2
- 소요 시간: 20분
- 알고리즘 : 구현 
'''
def solution(dirs):
    answer = 0
    visited = set()
    dir = {}
    dir['U'] = [0,1]
    dir['D'] = [0,-1]
    dir['R'] = [1,0]
    dir['L'] = [-1,0]
    cx  = 0
    cy = 0
    
    for d in dirs:
        nx = cx + dir[d][0]
        ny = cy + dir[d][1]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5 :
            continue
        tmp_s = str(min(cx,nx)) + str(max(cx,nx)) + str(min(cy,ny)) + str(max(cy,ny))
        if tmp_s not in visited:
            visited.add(tmp_s)
        cx = nx
        cy = ny
    answer = len(visited)
    return answer
