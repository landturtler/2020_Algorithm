#1806 부분합
#10000이하의 자연수로 이루어진 길이가 N인 수열이 주어질때, 연속된 수열의 부분합 중에 합이 S이상인 것 중 가장 짧은 길이 출력
#고민 : while문으로 right를 움직이면 right +1이 저장되느데, 만약 while문 없이 그냥 left하나 옮겨도 S보다 클 경우엔 right 값이 맞음 

MAX = 10000001

def solution(N,S,arr):
	answer = MAX
	left = right = 0
	interval_sum = 0

	for left in range(N):
		print("left = ",left,", right = ",right,", sum = ", interval_sum)
	
		#이미 부분합이 S이상이면 부분합 길이를 줄이기 위해 right를 왼쪽으로 이동 
		while left <= right and right < N and interval_sum >= S:
			print("sum에서",arr[right]," 만큼 뺌. right = ",right -1)
			interval_sum -= arr[right]
			right -= 1
		
		while right < N and interval_sum < S:
			interval_sum += arr[right]
			right += 1
		
		#부분합이 S이상일 때 해당 부분합의 길이 계산
		if interval_sum >= S:
			print("합이 S이상: ",left,", ",right,", ",interval_sum,", ")
			answer = min (answer,(right-left))
		interval_sum -= arr[left]
		
	if answer == MAX:
		answer = 0
	return answer

if __name__ == "__main__":
	N,S = map(int,input().split())
	arr = list( map(int,input().split()))
	answer= solution(N,S,arr)

	print(answer)

