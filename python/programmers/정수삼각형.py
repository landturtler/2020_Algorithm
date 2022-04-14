'''
알고리즘 : DP
풀이시간 : 20분
시간 오래걸렸던 것 : 프로그래머스에선 전역변수 사용 시 항상 global 붙이자

'''
dp = list()
N = 0

def go(i,j,triangle):
    if i < 0 or i >= N or j < 0 or j >= N:
        return 0
    
    if dp[i][j] != 0:
        return dp[i][j]
    
    dp[i][j] = max(go(i+1,j,triangle),go(i+1,j+1,triangle)) + triangle[i][j]
    return dp[i][j]

def solution(triangle):
    answer = 0
    global dp, N
    N = len(triangle)
    
    #1. dp배열 생성, dp[i][j] = dp[i][j]에서 탐색 시작했을때 최대 합 
    dp = [] * (N)
    for i in range(N):
        tmp_list = [0] * (i+1)
        dp.append(tmp_list)
        
    for i in range(N):
        dp[N-1][i] = triangle[N-1][i]
    
    # 2. dp 탐색
    go(0,0,triangle)
    answer = dp[0][0]
    return answer
        
    
    
