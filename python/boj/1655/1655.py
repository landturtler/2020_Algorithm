#1655 가운데를 말해요 
# 넣는 값 
import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_h, right_h = [], [] #중간값보다 작은값(최대힙),중간값보다 큰값(최소힙) . 중간값은 left_h의 루트값 

for i in range(N):
	x = int(input())
	#개수가 같으면 무조건 왼쪽힙에 넣어야 한다. 왼쪽힙의 값이 내가 원하는 중간값이므로 
	if len(right_h) == len(left_h):
		heapq.heappush(left_h, -x)
	#개수가 같지 않다면 오른쪽 힙에 넣는다. 힙 길이를 맞추기 위해 
	else:
		heapq.heappush(right_h, x)

	#넣고 나서 왼쪽 힙의 루트 > 오른쪽 힙의 루트 이면 둘을 바꿈 
	if right_h and -left_h[0] > right_h[0]:
		left_max = -left_h[0]
		right_min = right_h[0]
		heapq.heappop(right_h)
		heapq.heappop(left_h)
		heapq.heappush(left_h,right_min)
		heapq.heappush(right_h,left_max)
	
	#중간값 반환 : 왼쪽 힙의 최댓값
	print(-(left_h[0]))

