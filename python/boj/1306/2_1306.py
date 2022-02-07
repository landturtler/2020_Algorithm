#덱 사용하여 슬라이딩 윈도우 풀이
import collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
dq = deque()
answer = []

#초기값 저장
max_light = 0
for i in range(0,2*M-1):
	dq.append(tuple(arr[i],i))
	max_light = max( max_light, arr[i])
answer.append(max_light)

#한 칸씩 움직이기
for idx in range(2*M-1,N):
	

