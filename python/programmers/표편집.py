'''
Programmers Lv3
문제 : 표 편집을 수행한 결과로, 삭제된 행은 'x' 삭제되지 않은 행은 'O'을 표기하여 문자열 형태로 리턴
알고리즘 : 구현(링크드 리스트)
처음안 것 : O(n)으로 풀어야 하는 경우 양방향 linked list를 사용하는 방법도 생각해보자.
소요 시간 : 1시간(동안 풀다가 해설 참고함)
'''

def solution(n, k, cmd):
    answer = ['O'] * n
    up = [-1] + [x for x in range(n - 1)]  #up[i] :i번째 행 위 번호
    down = [x for x in range(1, n)] + [-1] #down[i] : i번째 행 아래 번호
    delete = [] #삭제되었던 행 번호, stack처럼 사용
    for c in cmd:
        op = c[:1]
        
        if op == 'D':
            num = int(c[1:])
            for _ in range(num):
                k = down[k]            
        
        elif op == 'U':
            num = int(c[1:])
            for _ in range(num):
                k = up[k]
        
        elif op == 'C':
            answer[k] = 'X'
            delete.append(k)
            # 삭제 후 인접 행 이동
            if up[k] != -1:
                down[up[k]] = down[k]
                
            if down[k] != -1:
                up[down[k]] = up[k]     
            
            # 현재 행번호 변경
            if down[k] == -1:
                 k = up[k]
            else:
                k = down[k]
                
        else:
            #가장 최근에 삭제되었던 행 번호
            d = delete.pop()
            
            # 인접 행 이동
            if up[d] != -1:
                down[up[d]] = d
                
            if down[d] != -1:
                up[down[d]] = d
                
            answer[d] = 'O'   
                
    return "".join(answer)
