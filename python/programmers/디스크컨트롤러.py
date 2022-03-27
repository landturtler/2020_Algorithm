'''
Programmers LV3
- 알고리즘 : 우선순위 큐
- 소요 시간 : 약 1시간 
- 주의 사항: 큐와 관련된 건 항상 조건문에 len(q) > 0을 붙이는 습관 들이기
            sort()는 반환값이 없는거고, sorted()는 list로 반환한다.  
'''
import heapq
from collections import deque
import math

def solution(jobs):
    answer = 0
    n_jobs = deque(sorted(jobs))
    cur_time = n_jobs[0][0] #현재 시간, 가장 첫번째 요청이 들어온 시간으로 초기화
    hq = []  #우선순위 큐. (소요시간, 요청시간)순으로 정렬
    
    while len(n_jobs) > 0 or len(hq) > 0:
        # 1. 우선순위 큐에 jobs들 넣기 
        # -- 현재 시간 이전에 요청이 들어온 job들을 우선순위 큐에 삽입
        if len(hq) == 0 and n_jobs[0][0] > cur_time:
            cur_time = n_jobs[0][0]
            
        while len(n_jobs) > 0 and n_jobs[0][0] <= cur_time:
            time,task = n_jobs.popleft()
            heapq.heappush(hq,[task,time])
    
        # 2. 디스크 실행하기 
        # -- 현재 실행 가능한 대상들 중 가장 소요 시간이 짧은 대상을 실행
        task, input_time = heapq.heappop(hq)
        answer += (cur_time - input_time) #대기시간
        answer += task #소요 시간
        cur_time += task

    return math.trunc(answer // len(jobs))
