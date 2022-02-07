#10000 이하 자연수로 이루어진 길이 N짜리 수열이 존재할때,연속된 부분합이 S이상 중, 가장 짧은 것의 길이는?
#유의할 것 : right포인터는 부분합의 마지막 요소 + 1이다! 

N, S = map(int,input().split())
arr = list(map(int,input().split()))
answer = 1000001

left = right = 0
inter_sum = 0 #중간의 합 

 while right < N:
 
 	# 부분합이 S이상인 경우, 부분합 길이를 구한 후, left 포인터로 옮김 
 	if iter_sum >= S:
		answer = min(answer,right-left)
		inter_sum -= arr[left]
		left += 1
	
	# 부분합이 S 미만인 경우, 
	else:
		inter_sum += arr[right]
		right += 1

if answer == 1000001
 	answer = 0

