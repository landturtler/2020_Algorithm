from itertools import permutations

lis = [0,0,1,1,1]

set_lis =set( permutations(lis,5) )
for x in set_lis:
	print(x)

