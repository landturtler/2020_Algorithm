from itertools import combinations
from string import ascii_lowercase

N, K = map(int,input().split())
except_char = set(['a','c','i','n','t'])
words = [ set(list(input())) - except_char for _ in range(N) ]
answer = 0

if K < 5:
	print(0)
	exit(0)

alpha = set( sum([ list(word) for word in words ], []) )
   
combs = combinations(alpha, min(len(alpha), K - 5))
for comb in combs:
	comb = set(comb)
	cnt = 0
	for word in words:
		if word <= comb:
			cnt += 1
	answer = max(answer, cnt)
print(answer)
