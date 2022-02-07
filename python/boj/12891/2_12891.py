#처음엔 매 번 count()값으로 슬라이싱한 문자열의 각 개수를 구하려 했는데, 그렇게 하면 시간초과 날 가능성이 있음
#투포인터, 슬라이딩 윈도우 

S,P = map(int,input().split())
dna = input()
a,c,g,t = map(int,input().split()) #최소로 필요한 문자 개수 
dic_cnt = { 'A' : 0, 'C':0,'G':0,'T':0} #부분 문자열에서 각 알파벳의 개수를 담는 딕셔너리 

answer = 0

for i in range(0,P):
	dic_cnt[ dna[i] ] += 1

if( dic_cnt['A'] >= a and dic_cnt['C'] >= c and dic_cnt['G'] >= g and dic_cnt['T'] >= t):
	answer += 1

for i in range(P,S):
	dic_cnt[ dna[i] ] += 1
	dic_cnt[ dna[i-P]] -= 1 
	
	if( dic_cnt['A'] >= a and dic_cnt['C'] >= c and dic_cnt['G'] >= g and dic_cnt['T'] >= t):
		answer += 1

print(answer)
	
	
