'''
문제 : N만큼 일을 했을 때, 남은 작업량^2들의 합의 최솟값 출력 
알고리즘 : 그리디 / 힙
소요 시간 : 20분
헷갈린 것 : TypeError: 'module' object is not subscriptable에러 발생 시 heapq.func()이 아닌 func()만 쓴건아닌지, 혹은 func이름으로 접근한 건 없는지 확인 
'''
import heapq
def solution(n, works):
    answer = 0
    
    #works를 내림차순 힙에 삽입
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
        
    #가장 큰 값부터 업무를 1씩 수행 
    N = n
    while N and hq[0] < 0:
        heapq.heappush(hq, (heapq.heappop(hq) + 1))
        N -= 1
    
    #합 계산
    while hq:
        val = heapq.heappop(hq)
        answer += (val * val)
        
    return answer
