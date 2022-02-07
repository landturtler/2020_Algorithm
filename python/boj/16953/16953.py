#16953 a->b
# 2를 곱하거나 1을 수의 가장 오른쪽에 추가할 때 필요한 연산의 최솟값은?
from collections import deque

answer = -1
A,B = map(int,input().split())
q = deque()
q.append([A,1])
while q:
	num, cnt = q.popleft()
	if num == B:
		answer = cnt
		break
	elif num > B:
		continue
	else:
		q.append( [num*2,cnt+1])
		q.append( [num*10+1,cnt+1])

print(answer)
