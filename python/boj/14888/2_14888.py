#dfs로 풀기 

numlist = []
max_value = -1000000000
min_value = 1000000000

def dfs(idx,value,plus,minus,multi,divid):
	if idx == N:
		global max_value, min_value
		max_value = max(max_value, value)
		min_value = min(min_value, value)
		return
	else:
		global numlist
		if plus > 0:
			dfs(idx+1,value + numlist[idx],plus-1,minus,multi,divid)
		if minus > 0:
			dfs(idx+1,value - numlist[idx],plus,minus-1,multi,divid)
		if multi > 0:
			dfs(idx+1,value * numlist[idx],plus,minus,multi-1,divid)
		if divid > 0:
			val = 0
			if value < 0 and numlist[idx] > 0:
				val = -( abs(value) // numlist[idx] )
			else:
			 	val = value // numlist[idx]
			dfs(idx+1,val,plus,minus,multi,divid-1)
	

def solution(arr,op_list):
	N = len(arr)
	global numlist
	numlist = arr.copy()
	plus, minus, multi, divid =  op_list[0], op_list[1],op_list[2],op_list[3]
	dfs(1,numlist[0],plus,minus,multi,divid)


if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split(" ")))
	op_list = list(map(int,input().split(" ")))

	solution(arr,op_list)
	print(max_value)
	print(min_value)

	
