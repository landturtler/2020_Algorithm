'''
단어 변환
알고리즘 : BFS
수행 시간 : 20분
배운 점 : 문자열 비교해서 다른 글자 수 찾기 = zip()함수 사용하기
탐색으로 풀 수 있었던 이유: 한번에 한 단어씩만 바꿀 수 있음 + 바꿀 수 있는 문자가 정해져 있음(그래프에서 길이 존재하는 것과 비슷한 맥락) + 타겟 단어(목적지)가 정해져 있음 + 최소 변환 과정을 알아야 함 
'''
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = [False] * len(words) #visited[i] : words[i]로 변환한 적 있는지 저장하는 리스트
    # 1. BFS 큐 생성 
    q = deque()
    q.append((begin,0))
    
    # 2. BFS 탐색 
    while q:
        tmp = q.popleft()
        curword,dis = tmp[0],tmp[1]

        if curword == target:
            answer = dis
            break
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            # 단어 변환이 가능한지 판단 
            diff = 0
            for a,b in zip(curword,words[i]):
                if a != b:
                    diff +=1
            # 현재 큐에서 뽑은 단어와 words[i]가 한 개의 알파벳만 차이가 나므로, 변환 가능
            if diff == 1:
                visited[i]= True
                q.append((words[i],dis+1))
    
    return answer
