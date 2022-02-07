#세그먼트 트리로 풀기

def init(start, end, idx):
	if start == end: #leaf 노드
		tree[idx] = arr[start]
		return tree[idx]
	mid = (start + end) // 2
	
	tree[idx] = max(init(start,mid,idx*2),init(mid+1,end,idx*2+1))
	return tree[idx]

def query(start,end,idx,q_left,q_right):
	#범위 벗어나는 경우
	if q_left > end or q_right < start:
		return 0
	#범위 내에 있는 경우
	if q_left <= start and q_right >= end:
		return tree[idx]
	
	mid = (start + end) // 2
	return max( query(start,mid,idx*2,q_left,q_right), query(mid+1,end,idx*2+1,q_left,q_right))


if __name__ == '__main__':

	N,M = map(int,input().split())
	arr = list(map(int,input().split()))
	tree = [0]* N * 4

	init(0,N-1,1)
	for idx in range(M-1,N-M+1):
		start = idx - (M-1)
		end = idx + (M-1)
		print(start, end, end = " ")
		print(tree)
		print( query(start,end,1,0,N-1), end = " " )



