'''
Programmers LV2
- 소요 시간 : 30분
- 문자열을 왼쪽으로 s칸만큼 회전시켰을 때 올바른 문자열이 되게 하는 x의 개수 출력
- 알고리즘 : 구현 (stack)
- 올바른 괄호 구하는 법: 여는 괄호는 stack에 넣고 닫는 괄호는 stack값 비교 후 pop
- 유의할 것 :stack.top()구할 땐 항상 len(stack)비교 후 넣기
'''
from collections import deque
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        s = list(s)
        s2 = s[i:] + s[:i]
        stack = []
        flag = True
        for j in range(len(s2)):
            x = s2[j]
            if x == '{' or x == '[' or x == '(':
                stack.append(x)
            else:
                if x == '}' and len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                elif x == ']' and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                elif x == ')' and len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
        if len(stack) == 0 and flag == True:
            answer += 1
    return answer
