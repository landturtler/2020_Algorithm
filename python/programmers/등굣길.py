'''
풀이 시간 : 15분
문제 : [1,1] -> [m,n]까지 가는 최단 경로의 수를 리턴 
알고리즘 : DP
해당 알고리즘인 이유 : 1)1000000007로 나눈 나머지에서 최단경로 개수가 매우 많음(메모이제이션없으면 연산량 많음)
                      2) 내가 어떤 위치에 도착할 경우의 수 = 내 위에 도착할 경우의 수 + 내 왼쪽에 도착할 경우의 수이므로
좌표 기준이 (1,1)에서 시작할 땐 직관적으로 보기 편하게 (M+1), (N+1)의 사이즈로 만들자 
'''
def solution(m, n, puddles):
    answer = 0
    dp = [ [0] * (m+1) for _ in range(n+1)]
    # 시작 지점 1저장
    dp[1][1] = 1
    
    # 웅덩이 위치에 -1을 저장
    for y,x in puddles:
        dp[x][y] = -1
    
    # 탐색 시작 
    for i in range(1, n+1):
        for j in range(1, m+1):
            #현재 위치가 웅덩이인지 확인
            if dp[i][j] == -1:
                continue
            
            #위 탐색
            if dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            
            #왼 탐색
            if dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]
    
    return dp[n][m] % 1000000007
