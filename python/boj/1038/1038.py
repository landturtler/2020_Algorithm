#1038 감소하는 수
# X의 자릿수가 큰수부터 작은 수까지 감소한다면 그 수를 감소하는 수라고 한다. N번째로 감소하는 수를 출력하라
# 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 ... 
# 1자리 수에서 감소하는 수 개수 : 9개 
# 2자리 수에서 감소하는 수 개수: (1+2+3+4+5+6+7+8+9 ) 
# 3자리 수에서 감소하는 수 개수 : 1+ (1+2) + (1+2+3) + (1+2+3+4) + 
#accumulate 함수는 itertools이고, 반드시 list()를 붙여야 함!!

from itertools import accumulate

def solution(N):
	answer = 0

	if N < 10:
		answer = N
		return answer
	elif N >= 10 and N <=45:
		N -= 9
		for i in range(1,10):
			for j in range(i):
				N -= 1
				if N == 0:
					answer = 10*i + j
					return answer
	#3자릿수 이상의 길이 찾기 
	else:
		N -= 45
		num = list(range(10))
		cul_num = list(accumulate(num)) #1,3,6,10,...
		
		first = 0 #첫번째 자리수
		second = 0 #두번째 자리수 
		for i in range(10,0,-1): #i = 10 -> 3, 9 ->4, 8->5, 
			for j in range(i): #j = 0~9
				N -= cul_num[j]
				if N < 0:
					first = 13 - i #총 자릿수
					second = 
					
		
					

if __name__ == "__main__":

	N = int(input())
	answer = 0

