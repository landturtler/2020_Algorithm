#11058 크리보드
# 버튼 N을 눌러서 화면에 출력된 A개를 최대로 하는 프로그램 작성하라
# dp와 buf를 따로 생성하면 X. 그리고 이전 값이 최대일대의 buf값이 항상 현재에도 최댓값을 주진 않는다??


N = int(input())
dp = [0]*(N+1)
buff = [0]*(N+1) #buf[i] :i번 버튼을 눌렀을 때 최댓값으로 A가 출력되는 경우, buf값
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):

    dp[i] = max(dp[i-1]+1, dp[i-1]+buff[i-1], 2*dp[i-3])
    if dp[i] == 2*dp[i-3]:
        buff[i] = dp[i-3]
    else:
        buff[i] = buff[i-1]
        
print(dp[N])
