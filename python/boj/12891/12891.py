#임의 문자열, 각 A,C,G,T의 최소 등장 횟수가 주어질 때 만들 수 있는 비밀번호의 수 출력. 단 문자열의 위치가 다르면 다른 문자열로 취급

S,P = map(int,input().split())
DNA = input()
min_cnt = list(map(int,input().split()))


answer = 0

for start_index in (0,S-P-1):
	sub_dna = DNA[start_index:start_index+P]
	if (sub_dna.count('A') >= min_cnt[0] and sub_dna.count('C') >= min_cnt[1] and sub_dna.count('G') >= min_cnt[2] and sub_dna.count('T') >= min_cnt[3]):
	 	answer += 1

sub_dna = DNA[S-P:]
if (sub_dna.count('A') >= min_cnt[0] and sub_dna.count('C') >= min_cnt[1] and sub_dna.count('G') >= min_cnt[2] and sub_dna.count('T') >= min_cnt[3]):
	answer += 1

print(answer)
				

