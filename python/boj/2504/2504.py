#2504 괄호의 값
#가장 안쪽 ():2, 가장 안쪽 []:3, (x) : 2*x, [x] : 3*x, xy = x+y
# 파이썬은 stack 없음. 큐랑 stack 둘다 deque 사용함. top대신 s[-1] 사용 

#stack에 괄호열만 넣지 말고, 각 계산값을 넣을 수 있음. ( [] () [[]] ) 등으로 있을 때 ( 3 + 2 + 9 ) -> 2*(3+2+9)여야 하므로.. 
#stack에 int형이랑 str값이랑 섞이면 불편하므로 int형도 str()로 바꾼 후 stack에 넣기
#stack에 값 접근할땐 항상 비어있는지 확인할 것 
from collections import deque

def solution( st ):
	answer = 0
	s = deque() #stack
	s.append(st[0])

	for i in range(1,len(st)):
		x = st[i]
		if x == '(' or x == '[':
			s.append(x)

		elif x == ')':
			tmp = 0
			if len(s) == 0: or s[-1] == '[':
				return 0
			elif s[-1] == '[':
				return 0

			elif s[-1] == '(':
				tmp = 1

			else:
				tmp = int(s.pop())
				while len(s) != 0 and s[-1].isdigit() == True:
					tmp += int(s.pop())
				if len(s) == 0 or s[-1] == '[':
					return 0
			s.pop()
			s.append(str(tmp*2))

		elif x == ']':
			tmp = 0
			if len(s) == 0 or s[-1] == '(':
				return 0

			elif s[-1] == '[':
				tmp = 1
			else:
				tmp = int(s.pop())
				while len(s) != 0 and s[-1].isdigit() == True:
					tmp += int(s.pop())
				if len(s) == 0 or s[-1] == '(':
					return 0
			s.pop()
			s.append(str(tmp*3))
	
	#stack에 괄호가 남아있는 경우 잘못된 괄호
	if '(' in s or '[' in s or len(s) == 0:
		return 0

	answer = sum( list( int(x) for x in s) )
	return answer
		

if __name__ == "__main__":
	st = input()
	answer = solution(st)
	print(answer)
