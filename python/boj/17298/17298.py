#17298 오큰수
# 크기가 N인 수열이 주어질 때, 오큰수 NGE(i) = Ai의 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수. 만약 그런 수가 없는 경우 -1을 출력하라

from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	answer = [-1] * N #오큰수를 저장하는 배열 
	stack = deque() 

	for i in range(N):
		# arr[i]값이 stack.top()보다 크다는 것은, stack.top()번째의 오큰수가 arr[i]라는 의미
		while stack and arr[stack[-1]] < arr[i]:
			answer[stack.pop()] = arr[i] 

		stack.append(i)

	for i in range(N):
		print(answer[i], end = ' ')


		
	
	

