import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	alist,blist,clist,dlist = [], [], [], []

	for _ in range(N):
		a,b,c,d = map(int,input().split())
		alist.append(a)
		blist.append(b)
		clist.append(c)
		dlist.append(d)
	
	#ab의 합 딕셔너리 생성
	ab = {}
	result = 0

	for a in alist:
		for b in blist:
			if a+b not in ab:
				ab[a+b] = 1
			else:
				ab[a+b] += 1
	
	for c in clist:
		for d in dlist:
			if -(c+d) in ab:
				result += ab[-(c+d)]

	print(result)
