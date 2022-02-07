#16916 부분 문자열
#문자열 S,P가 주어질 때 P가 S의 부분 문자열이면 1 아니면 0을 출력하라
# KMP 알고리즘 :
# pi[i] : 0~i까지의 부분 문자열 중 prefix == suffix인 부분 문자열의 가장 긴 것의 길이 단, i < len(S) --> 이건 부분문자열에 대해 구하는것임!!!!! 
'''a
ABAABAB이라하면 ,
pi[0] : A = 0
pi[1] : AB = 0
pi[2] : ABA - 양 끝의 A가 같음 = 1
pi[3] : ABAA - 양 끝의 A가 같음 = 1
pi[4] : ABAAB - 양 끝의 AB가 같음 = 2
pi[5] : ABAABA - 양 끝의 ABA가 같음 = 3
'''
#아니 kmp찾을 땐 또 megin = matched = 0으로 시작함 

def get_partial_match(S):
	begin = 1
	matched = 0 #탐색할 prefix 문자 위치 겸, pre=suf인 부분 문자열의 길이 
	pi = [0] * (len(S))
#비교할 문자가 S의 끝에 도달할 때까지 부분일치 기록 
	while begin + matched < len(S):
	 	#S[matched]와 같은 글자가 S[begin+matched]위치에 존재하는 경우
		if S[begin + matched] == S[matched]:
			matched += 1
			pi[begin+matched-1] = matched #begin+matched까지 부분 문자열은 matched길이로 prefix= subfix를 만족한다 
		else:
			#맨 처음글자와 일치하는 위치까지 begin++ 
			if matched == 0:
				begin += 1
			# 현재 불일치가 발생한 위치는 begin +matched
			# 매칭을 진행하면서 구했었던 접두/접미사 길이만큼 탐색을 건너뒬 수 있다. 접두/접미사 길이가 pi[matched-1]임 
			else:
				begin += matched - pi[matched-1]
				matched = pi[matched - 1]
	return pi


def kmp_search(S,P):
	answer = 0
	N = len(S)
	M = len(P)
	pi = get_partial_match(P)
	begin = matched = 0

	while begin <= (N-M) :
	#	print("begin :",begin,", match = ", matched)
	#	print( "S[begint+match] = ",S[begin+matched], " P[match] = ",P[matched])
		#P[begin+matched]와 S[matched]가 동일할 경우 matched ++
		if matched < M and S[begin+matched] == P[matched]:
	#		print(" S[",begin + matched,"] = P[",matched,"] ,matched = ",matched+1)
			matched += 1

		#문자열이 모두 일치함 
			if matched == M:
				answer = 1
				break

		else:
		 	#일치부분 없을 때 다음 문자부터 탐색 
			if matched == 0:
				begin += 1
			#문자열 불일치. 접두사, 접미사 길이만큼 건너 뀜
			else:
				#접두/접미사 길이인 pi[matched-1]을 빼주면 다음 탐색의 시작 위치. begin은 증가, matche는 감소
	#			print("begin = ",begin,", matched = ",matched,", pi[matched-1]")
				begin += (matched - pi[matched-1])
				matched = pi[matched-1]

	return answer 

if __name__ == "__main__":
	S = input()
	P = input()
	answer = kmp_search(S,P)
	print(answer)
		
