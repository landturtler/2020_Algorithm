
#변수 선언 
K, N = map(int,input().split())
arr = []

for i in range(K):
	arr.append(int(input()))

#가장 긴 길이 기준으로 이분 탐색
start = 1 
end = max(arr)
result = 0

while start <= end:
	mid = (start + end ) // 2 
	count = 0 
	
	#길이가 mid인 랜선으로 자를 때 만들 수 있는 랜선 개수 탐색
	for i in arr:
		count += ( i // mid )
	 
	#랜선 개수가 N이 될 때까지 탐색 진행
	if count >= N:
		result = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)

