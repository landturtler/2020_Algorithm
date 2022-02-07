#동전 0
#N종류의 동전이 있을때, 합을 k로 만들 수 있는 최소 동전 개수
#단 동전끼리는 배수 단위



def solution(K, coins):
	answer = 0 
	if K in coins:
		answer = 1
	else:
		idx = 0
		for i in range(len(coins)-1,0,-1):
		 if coins[i] < K:
				idx = i
				break
		while K > 0:
			tmp =	K // coins[idx]
			answer += tmp
			K -= coins[idx] * tmp
			idx -= 1
	return answer

if __name__ == "__main__":
	N,K = map(int,input().split())
	coins = [ int(input()) for _ in range(N) ]
	answer = solution(K,coins)	
	print(answer)

