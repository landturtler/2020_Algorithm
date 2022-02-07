#괄호는 무조건 스택@@ 스택엔 값이 들어가도 된다

from collections import deque

st = input()
s = deque()
answer = 0

for i in range(len(st)):
	x = st[i]
	if x == '(' or x == '[':
		s.append(x)
	
	elif x == ')': #스택에 (값을 찾아야 함 
		tmp = 0 
		if len(s) == 0 or s[-1] == '[': 
			return 0  
		elif s[-1] == '(':
			tmp = 1
		#숫자가 있으면, '('가 나올 때까지 숫자들을 더함
		else:
			tmp = int(s.pop())
			while len(s) != 0 and s[-1].isdigit() == True:
				tmp += int(s.pop())
			if len(s) == 0 or s[-1] == '[':
				return 0
			#숫자들은 다 뺐고, 그다음 스택 top이 '('이면
			s.pop()
			s.append(str(tmp*2))

	elif x == ']':
		tmp == 0
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
	
	#스택에 괄호가 남아있는 경우 잘못된 괄호
	if len(s) == 0: #값이 아무것도 없는 경우
		return 0 
	elif '(' in s or '[' in s:
		return 0
	
	answer = sum(list( int(x) for x in s))




		#중간에 숫자가 있으면 (가 나올 때까지 숫자들을 더함

