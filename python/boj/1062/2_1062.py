#for문 돌 때 for i in arr: i.remove(i)하면 원본 데이터가 훼손되어서 모든 루프를 돌지 못한다. 
# 문자열을 슬라이싱하면 시간이 오래 걸림 

#for word in words: word = word[4:-3] 하면 원본 데이터는 수정 안됨 
from itertools import combinations
from string import ascii_lowercase

def solution(N,K,words):
	answer = 0
	
	#a,c,i,t,n을 읽지 못하면 모든 글자를 읽을 수 없음 
	if K < 5:
		return 0

	#단어 문자열에 a,c,i,n,t 글자 삭제
	exceptChar = ['a','c','i','n','t']

	for exc in exceptChar:
		words = [ word.replace(exc,'') for word in words ]
	
	#단어에 있는 알파벳 추출 
	alpha = []
	for word in words:
		for x in word:
			if x not in alpha:
				alpha.append(x)
	
	for comb in combinations(alpha,K-5):
		comb = list(comb)

		cnt = 0
		for word in words:
			is_poss = True
			for x in word:
				if x not in comb:
					is_poss = False
					break
			if is_poss == True:
				cnt += 1

		answer = max(answer,cnt)

	return answer 


if __name__ == "__main__":
	N,K = map(int,input().split())
	words = [ input() for _ in range(N) ]

	answer = solution(N,K,words)
	print(answer)
