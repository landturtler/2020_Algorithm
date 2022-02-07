#14719 빗물
# 투포인터 문제. 가장 큰 높이의 높이 & 인덱스를 찾고 왼쪽 -> 탑. 오른쪽 -> 탑까지 꾸준히 더해줌
# 조건 : 현재 위치보다 양쪽에 더 높은 블록이 존재하면 현재 위치에 빗물이 고인다. 
# 현재위치의 왼쪽 블록 중 가장 큰 높이(a), 현재위치의 오른쪽 블록 중 가장 큰 높이(b)를 찾고 min(a,b) - 현재 높이 값들을 더해나감. 단 현재 높이가 a,b보다 클 수 있으니 a,b의 초기값을 현재 높이로 설정하기


def solution(H,W,arr):
	answer = 0 
	
	for i in range(1,W-1):
		left = max(arr[:i+1]) #현재 높이가 더 높을 수 있으므로 현재 높이까지 비교하기 
		right = max(arr[i:])
		answer += ( min(left,right) - arr[i] )
		
	return answer

if __name__ == "__main__":
	H,W = map(int,input().split(" "))	
	arr = list(map(int,input().split()))
	answer = solution(H,W,arr)
	print(answer)

