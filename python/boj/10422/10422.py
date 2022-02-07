#10422 괄호
# 길이가 L인 서로 다른 올바른 괄호 문자열의 개수. 단 올바른 괄호가 s라 하면 (S)와 S*S도 올바른 괄호이다.
#dp[i] : 길이가 i인 올바른 괄호 개수 = dp[i-2] + dp[i-k]*dp[k]
def solution(N):
	

if __name__ == "__main__":
	N = int(input())
	answer = solution(N)
	print(answer)
