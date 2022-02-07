#9935 문자열 폭발
# 문자열 입력받을 때 그냥 input()을 받으면 엔터도 함께 들어간다

import sys
input = sys.stdin.readline

if __name__ == "__main__":
	s = input().rstrip()
	bom = input().rstrip()

	stack = []
	for x in s:
		stack.append(x)

		#스택 내에 폭발 문자열 있는지 확인하고 있으면 삭제  
		if "".join(stack[-len(bom):]) == bom:
			del stack[-len(bom):]
	
	# 스택 내 총 길이 확인 
	if len(stack) == 0:
		print("FRULA")
	
	else:
		print("".join(stack))

