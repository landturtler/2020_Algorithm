#1062 가르침
#N개의 글자가 있고, k개의 알파벳만 가르칠 수 있을때 읽을 수 있는 글자의 최댓값
#모든 단어는 anta로 시작하고 tica로 끝난다
#순열 조합은 collections가 아니라 itertools임. collections는  큐슬때..
#알파벳 -> 아스키 코드 : ord() , 숫자 -> 알파벳 : chr()
#리스트 삭제 : remove(삭제할 값), pop(인덱스) 
#combinations 결과 쌍은 tuple단위로 저장이 된다. 
# python 자료구조 출력하는 방법
#알파벳 리스트 만드는 법 : from string import ascii_lowercase(uppdercase)
#조합 시간 복잡도; 

from string import ascii_lowercase
from itertools import combinations

def solution(N,K,words):
	answer = 0
	if K < 5:	 #anta, tica를 읽을 수 없음 
		return 0
	
#	alpha = list( chr(x) for x in range(97,97+26))
	alpha = list(ascii_lowercase)
	alpha.remove('a')
	alpha.remove('c')
	alpha.remove('i')
	alpha.remove('n')
	alpha.remove('t')
	
	#a,c,i,n,t는 무조건 읽어야 하는 문자이므로 word에서 해당 글자 삭제

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
		answer = max(answer, cnt)

	return answer


if __name__ == "__main__":
	N,K = map(int,input().split(" "))
	words = list( input() for _ in range(N) )

	answer = solution(N,K,words)
	print(answer)

