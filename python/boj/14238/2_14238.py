
dp = []
N = 0

def go(ac,bc,cc,p1,p2):

	if ac < 0 or bc < 0 or cc < 0:
		return False
	
	if ac == a and bc == b and cc == c:
		return True
	
	if dp[ac][bc][cc][p1][p2]:
		return False
	
	dp[ac][bc][cc][p1][p2 = True
	
	if ac + 1 <= a:
		ans[ac+bc+cc] = '
	
	if ac <

if __name__ == "__main__":
	S = input()
	a = S.count('A')
	b = S.count('B')
	c = S.count('C')
	N = len(S)
	
	#dp[a][b][c][p1][p2] : A가 a번,B가 b번,C가 c번 출근했고, 직전날에 p1이 직직전 날에 p2가 출근하는 경우가 가능한지 
	dp = [[[[[[-1] for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

