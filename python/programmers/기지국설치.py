'''
Programmers LV3
- 알고리즘 : 구현 
- 소요시간 : 1시간(예전에 c++로푼적잇음)
- 이분탐색인줄 알았으나, 기지국 개수를 세어야 하는 것이기 때문에 이분탐색도 애매
- 각 기지국이 설치된 위치를 돌면서, 인접한 기지국 사이에 전파가 도달하지 못하는 집이 있으면 기지국을 설치함. 이 때 설치할 기지국의 개수 : (도달하지 못한 집의 개수) // (2 * W + 1) + 1(만약 2 * W +1로 나누어떨어지지 않는다면)
- 헷갈리지 말 것 : station의 인덱스는 1 ~ N까지라는 것! 
- point : 기존에도 station이 있었고, 추가로 설치해야 할 기지국을 구해야 하므로 기존 station들의 위치를 돌면서 전파가 도달하지 못한 곳 찾기
'''

def solution(n, stations, w):
    answer = 0
    len = 0 #인접한 기지국 사이에 전파가 도달하지 않는 집의 개수 
    left = 1 #left : 이전 기지국이 도달가능한 가장 오른쪽 집 + 1
    right = 0  # right : 현재 기지국이 도달가능한 가능한 가장 왼쪽 집 - 1
    for station in stations:
        right = station - w - 1
        if left <= right:
            len = right - left + 1 
            
            #새로운 기지국 설치
            answer += (len//(2 * w + 1))
            if len % (2 * w + 1) > 0:
                answer += 1
        left = station + w + 1
        
        if left > n :
            break
            
    # 가장 오른쪽 처리(가장 마지막에 설치했었던 기지국으로는 끝까지 전파가 도달하지 못할 경우)
    if left <= n:
        len = n - left + 1
        answer += (len // (2 * w + 1))
        if len % (2 * w + 1) > 0:
            answer += 1
            
    return answer
