# 3085 사탕 게임a
# 인접한 두 사탕의 자리를 1번 바구고. 그 때 같은 색으로 이루어지는 가장 긴 연속부분을 고른 다음 사탕을 먹을 때 먹을 수 있는 사탕의 최대 개수
#리스트에서 각 원소의 빈출 횟수를 리스트로 만들어주는 라이브러리: Counter(), most_common(i) #가장 많이 나온 상위 i개의 리스트를 출력
# ch = collections.Counter(arr[i]).most_common(1)[0]
# swap : a,b = b,a 로 바꾸면 swap됨. arr[a],arr[b] = arr[b],arr[a]
# str은 수정/삭제가 안되므로 입력받을 때 split()으로 나눠서 저장하기
# str을 철자 하나씩 끊어 list로 저장하는 법 : list(S)로 하기!!!

import collections

def search(i,j):
	#상하좌우로 해당 색의 사탕이 연속으로 몇 개 있는지 탐색
	candy = arr[i][j]
	cnt_1 = 1
	cnt_2 = 1

	#위 방향으로 연속으로 몇 개 있는지 확인
	idx = j-1
	while idx >= 0 and arr[i][idx] == candy:
		cnt_1 += 1
		idx -= 1

	#아래 방향으로 연속 몇 개 있는지 확인
	idx = j+1
	while idx < N and arr[i][idx] == candy:
		cnt_1 += 1
		idx += 1

	#왼쪽 방향으로 연속 몇 개 있는지 확인
	idx = i - 1
	while idx >= 0 and arr[idx][j] == candy:
		cnt_2 += 1
		idx -= 1
	
	#오른쪽 방향으로 연속 몇 개 있는지 확인
	idx = i + 1
	while idx < N and arr[idx][j] == candy:
		cnt_2 += 1
		idx += 1
	return max(cnt_1,cnt_2) 

if __name__ == "__main__":

	N = int(input())
	arr = [ list(input()) for _ in range(N) ]
	answer = 0

	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	for i in range(N):
		for j in range(N):
			for k in range(4):
				nx = i + dx[k]
				ny = j + dy[k]
			
				if nx < 0 or nx >= N or ny < 0 or ny >= N:
					continue
				
				#swap한 값으로 개수 탐색 
				arr[i][j], arr[nx][ny] = arr[nx][ny],arr[i][j]	
				answer = max(answer,search(i,j))
				arr[i][j], arr[nx][ny] = arr[nx][ny],arr[i][j]
			
	print(answer)
