#14238 출근기록
#dp[i][3] : 길이가 i이고 마지막 문자가 0(A), 1(B), 2(C)인 string값 ? 근데 그 값을 알고 잇어야 해서..경우의 수로는 안될 것 같은데미..
#고민한 것 :top-down으로 하면 dp배열에 값이 있을 때 dp배열값을 리턴하느데, 이건 경우의 수나 숫자값도 아니고 '배열'값을 리턴해야 해서.. top-down으로 풀이가 가능할지 고민
# 2번째 줄처럼 하려면 
#dp배열에 필요한 것 :출근기록, 남은a b c횟수 a
#bfs로 풀어보기 : 큐에 (len(S), S, a,b,c적기)
#dp배열에 하나의 값만 들어간다면, 그 직전수를 쓸수 없는 경우가 발생할 수 있다.

from heapq import heappush, heappop

if __name__ == "__main__":
	S = input()
	a = S.count('A')
	b = S.count('B')
	c = S.count('C')
	answer = ""
	dp = list( for _ in range(len(S)+1)) #dp[i][3] = 길이가 i이고 마지막 문자가 0(A),1(B), 2(C)인 대상들 저장
	dp_a = list(set([]) for _ in range(len(S)+1))
	dp_b = list(set([]) for _ in range(len(S)+1))
	dp_c = list(set([]) for _ in range(len(S)+1))


	hq = []
	if a > 0:
		heappush(hq,[-1,'A',a-1,b,c])
		dp_a[1].add('A')

	if b > 0:
		heappush(hq,[-1,'B',a,b-1,c])
		dp_b[1].add('B')

	if c > 0:
		heappush(hq,[-1,'C',a,b,c-1])
		dp_c[1].add('C')

	while hq:
		cur = heappop(hq)
		le = -1*cur[0]
		cur_s = cur[1]
		cur_a = cur[2]
		cur_b = cur[3]
		cur_c = cur[4]
	
		if cur_a == 0 and cur_b == 0 and cur_c == 0:
			answer = cur_s
			break
		
		elif cur_s[-1] == 'A' and  len(dp_a[-1*(le+1)]) > 0:
			continue
		elif cur_s[-1] == 'B' and len(dp_b[-1*(le+1)]) > 0:
			continue
		elif cur_s[-1] == 'C' and len(dp_c[-1*(le+1)]) > 0:
			continue

		#a인 경우 삽입
		if cur_a > 0:
			heappush(hq,[-1*(le+1),cur_s + 'A', cur_a -1, cur_b,cur_c])
			dp_a[-1*(le+1)],add( cur_s +'A') 

		if cur_b > 0 and cur_s[-1] != 'B':
			heappush(hq,[-1*(le+1),cur_s + 'B', cur_a, cur_b-1,cur_c])
		if cur_c > 0 and len(cur_s) >= 2 and cur_s[-1] != 'C' and cur_s[-2] != 'C':
			heappush(hq,[-1*(le+1),cur_s + 'C', cur_a, cur_b,cur_c])

	print(answer)
