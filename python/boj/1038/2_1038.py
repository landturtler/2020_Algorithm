#큐를 이용하여 푸는 방법 : 기존에 감소하는 수로 판별된 숫자를 큐에 넣고 마지막 자리에 작은 숫자들을 넣어감 
#defaultdict는 collections

from heapq import heappush, heappop
import sys

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	answer = 0
	nums = [] #감소하는 수를 순서대로 저장 
	hq = []
	
	if N <= 10:
		answer = N
	
	else:
		for idx in range(1,10):
			heappush(hq,idx)
			nums.append(idx)

		while idx < N and hq:
			cur_n = heappop(hq)

			for i in range(cur_n%10):
				heappush(hq,cur_n*10 + i)
				nums.append(cur_n*10 + i)
				idx += 1
	
	if len(nums) < N:
		answer = -1
	else:
	 	answer = nums[N-1]
	
	print(answer)

			
