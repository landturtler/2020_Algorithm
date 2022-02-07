#1700	멀티탭	스케줄링
#멀티탭의	구	개수가	주어지고,	전기용품을	사용하는	순서가	주어질	때,	최소로	멀티탭을	뺄	수	있는	횟수	출력	
#dp나	완전탐색	하려했는데,	dp는	현재	멀티탭의	배열을	알고	있어야	하지	않나?	그럴	거면	그냥	완전탐색	할까	
# 완탐 안되는 이유 : N =2, K = 100일때 98번동안 둘 중에 하나를 뽑아야 하는 경우의 수로 2^98제곱이 됨
# dp랑 그리디 중 선택해야 함. 
# 리스트 내에서 특정 값의 인덱스 찾기 : index()함수. 만약 여러 인덱스를 잧고 싶을땐 enumerate 사용하기
# result = [ idx for idx,value in enumerate(arr) if value == 값 ]
#나는 처음에 무조건 가장 마지막 인덱스를 뽑는건 줄 알았는데, 멀티탭에 있는 대상들이 이후에 다시 나온다면, 처음으로 나오는 위치가 제일 늦은 걸 찾는거임! ex) 2 4 3이 꽃혀있고 5를 넣어야 함. 그 다음 arr가 4 3 2라고 하면 2를 뽑아야 함. 그래야 5 4 3 -> 5 4 3 -> 2 4 3 으로 한번만 뽑을 수 있음

def	solution(N,K,arr):
	answer = 0
	if N >= K:
		return 0
	
	#처음 N개 멀티탭에 삽입
	multi_tap = []
	cnt = 0
	for start in range(K):
		if arr[start] not in multi_tap:
			multi_tap.append(arr[start])
			cnt += 1
			if cnt == N:
				break
	
	#N+1~K번째로 사용할 전기기구를 어디에 넣을지 선택 
	for i in range(start+1,K):
		#i번째로 사용할 기구가 이미 멀티탭에 있는 경우  
		if arr[i] in multi_tap:
			continue
		
		#멀티탭에 있는 대상 중 앞으로 다시 쓰이지 않는 대상 탐색 
		check_selected = False
		for mt in multi_tap:
			if mt not in arr[i+1:]:
				delete_idx = multi_tap.index(mt)
				multi_tap[delete_idx] = arr[i]
				check_selected =  True
				answer += 1
				break
		
		#멀티탭에 모든 대상이 이후에 다시 쓰이면, 가장 마지막으로 쓰이는 전기 기구를 뽑음
		if check_selected == False:
			max_idx = -1
			delete_idx = 0
			for mi in range(N):
				mt = multi_tap[mi]
				tmp_idx = arr[i+1:].index(mt)
				if max_idx < tmp_idx:
					max_idx = tmp_idx
					delete_idx = mi
		
			multi_tap[delete_idx] = arr[i]
			answer += 1

	return answer 


if	__name__ ==	"__main__":
	N,K	= map(int,input().split())
	arr	= list(map(int,input().split()))

	answer = solution(N,K,arr)
	print(answer)

