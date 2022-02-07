
MAX = 1000001

def solution(N,S,arr):
	answer = MAX
	left = right = 0
	interval_sum = 0
	
	while True:
		if interval_sum >= S:
			answer = min(answer, right-left)
			interval_sum -= arr[left]
			left += 1

		elif right == N:
			break

		else:
			interval_sum += arr[right]
			right += 1

	if answer == MAX:
		answer = 0
	
	return answer

if __name__ == "__main__":
	N,S = map(int,input().split())
	arr = list(map(int,input().split()))

	answer = solution(N,S,arr)
	print(answer)

