#1700	멀티탭	스케줄링
#멀티탭의	구	개수가	주어지고,	전기용품을	사용하는	순서가	주어질	때,	최소로	멀티탭을	뺄	수	있는	횟수	출력	
#dp나	완전탐색	하려했는데,	dp는	현재	멀티탭의	배열을	알고	있어야	하지	않나?	그럴	거면	그냥	완전탐색	할까	
# 완탐 안되는 이유 : N =2, K = 100일때 98번동안 둘 중에 하나를 뽑아야 하는 경우의 수로 2^98제곱이 됨
# dp랑 그리디 중 선택해야 함. 
# 리스트 내에서 특정 값의 인덱스 찾기 : index()함수. 만약 여러 인덱스를 잧고 싶을땐 enumerate 사용하기
# result = [ idx for idx,value in enumerate(arr) if value == 값 ]


def	solution(N,K,arr):
	answer = 0	
			
	multi_tap =	arr[:N]	#맨	처음 N개만큼은 arr순서대로 삽입
	#N+1~K번째로 사용할 전기기구를 어디에 넣을지 선택 
	for i in range(N,K):
		
		#idx번째로 사용할 기구가 이미 멀티탭에 있는 경우  
		if arr[i] in multi_tap:
			continue
		
		#멀티탭에 있는 대상이 앞으로 몇번째 인덱스에서 나오는지 찾고 가장 큰 인덱스값 찾기
		max_idx = -1
		delete_idx = 0 #빼야하는 멀티탭 인덱스 
		for mi in range(N):
			cur = multi_tap[mi]
			tmp = list(x for x,value in enumerate(arr[i+1:]) if value == cur)
			if len(tmp) == 0:
				delete_idx = mi
				break
			else:
				if max_idx < max(tmp):
					max_idx = max(tmp)
					delete_idx = mi
		multi_tap[delete_idx] = arr[i]
		answer += 1
	
	return answer 


if	__name__ ==	"__main__":
	N,K	= map(int,input().split())
	arr	= list(map(int,input().split()))

	answer = solution(N,K,arr)
	print(answer)

