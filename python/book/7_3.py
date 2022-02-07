#떡볶이 떡 만들기

N,M = map(int,input().split())
array = list(map(int,input().split()))

min_height = 1
max_height = max(array) - 1
answer = 0

while min_height <= max_height:
	mid = int((min_height + max_height) / 2)
	temp_sum = 0
	for x in array:
		if x > mid:
			temp_sum += ( x - mid )
	if temp_sum >= M:
		answer = max(mid,answer)
		min_height = mid + 1
	else:
		max_height = mid - 1

print(answer)

