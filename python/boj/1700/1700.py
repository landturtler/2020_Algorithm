#1700	멀티탭	스케줄링
#멀티탭의	구	개수가	주어지고,	전기용품을	사용하는	순서가	주어질	때,	최소로	멀티탭을	뺄	수	있는	횟수	출력	
#dp나	완전탐색	하려했는데,	dp는	현재	멀티탭의	배열을	알고	있어야	하지	않나?	그럴	거면	그냥	완전탐색	할까	
# 완탐 안되는 이유 : N =2, K = 100일때 98번동안 둘 중에 하나를 뽑아야 하는 경우의 수로 2^98제곱이 됨
# dp랑 그리디 중 선택해야 함. 

electro	=[]
max_cnt	= 101

def	go(idx,cnt,arr):
	global max_cnt
	if idx == K:
		max_cnt	= min(max_cnt, cnt)
		return	

#이미	멀티탭에	이번	전기용품이	있다면	뽑지	않고	넘어감
	if max_cnt < cnt:
		return

	elif electro[idx] in arr:
		go(idx+1,cnt,arr)
		
	else:
		for	i in range(N):
			tmp	= []
			tmp = arr.copy()
			tmp[i] = electro[idx]
			go(idx+1,cnt+1,tmp)

def	solution(N,K,arr):
	global electro,max_cnt
	electro	= arr.copy()
	
	multi_tap =	arr[:N]	#맨	처음	N개만큼은	arr순서대로	삽입
	go(N,0,multi_tap)

	return max_cnt


if	__name__ ==	"__main__":
	N,K	= map(int,input().split())
	arr	= list(map(int,input().split()))

	answer = solution(N,K,arr)
	print(answer)

