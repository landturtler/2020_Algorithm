import sys
input = sys.stdin.readline
maxvalue = 0
minvalue = sys.maxsize()

def dfs(idx,value,plus,minus,multi,divid):
	if idx == N:
		global maxvalue, minvalue
		maxvalue = max(maxvalue,value)
		minvalue = min(minvalue,value)
		return
	else:
		if plus > 0:
			dfs(idx+1,value + num[idx], plus-1,minus,multi,divid)
		if minus > 0:
			dfs(idx+1,value - num[idx], plus,minus-1,multi,divid)
		if multi > 0:
			dfs(idx+1,value * num[idx], plus,minus,multi-1,divid)
		if divid > 0:
			val = 0
			if value < 0 and num[idx] > 0:
				val = - ( abs(value) // num[idx])
			else:
				val = value // num[idx]
			dfs(idx+1,val,plus,minus,multi,divid-1)


N = int(input())
num = list(map(int,input().split()))
opers = list(map(int,input().split()))
plus,minus,multi,divid = opers[0], opers[1], opers[2], opers[3]
dfs(1,num[0],plus,minus,multi,divid)


