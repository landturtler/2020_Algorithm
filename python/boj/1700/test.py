import sys

N,K = map(int,input().split())
arr = list(map(int,input().split()) #멀티탭 번호
answer = 0
multi_tap = [ ] #각 멀티탭에 들어있는 번호 

#멀티탭이 다 찰 때까지 넣기
if K <= N:
	answer = 0

#처음 N개 멀티탭 삽입
cnt = 0
for start in range(K):
	if arr[start] not in multi_tap:
		multi_tap.append(arr[start])
		cnt += 1

		if cnt == N: #N개 다 채웠을 경우
			break

#N+1~K번째 전기기구 선택
for i in range(start+1,K):
	if arr[i] in multi_tap:
		continue

	#N개 멀티탭 중 앞으로 한번도 안쓰이는 대상 탐색
	check = False
	for mt in multi_tap:
		if not in arr[i+1:]:
			delete_idx = multi_tap.index(mt)
			multi_tap[delete_idx] = arr[i]
			check = True
			answer += 1 #멀티탭을 뽑음
			break

	#모든 멀티탭이 다 쓰이면 , 현재시점으로부터 

#리스트에서 특정값의 모든 인덱스를 저장하는 법

result = [ idx for idx,value in enumerate(arr)




