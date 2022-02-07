#연산자 끼워넣기 
# N개의 수로 이루어진 수열이 주어지고, 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어질 때 만ㄷ르 수 있는 최대값과 최소값을 출력
#리스트에 리스트 추가 : extend(리스트)
# 조합 만들 때 중복 데이터가 있을 때 => permutation결과값을 set에 저장하고 다시 list로 만들기 
# 10억 
from itertools import permutations

def caculate_num(arr,op):
	result = arr[0]

	for idx in range(N-1):
		if op[idx] == '+':
			result += arr[idx+1]
		elif op[idx] == '-':
			result -= arr[idx+1]
		elif op[idx] == '*':
			result *= arr[idx+1]
		else:
			if result < 0 and arr[idx+1] > 0:
				result = -( abs(result) // arr[idx+1])
			else:
				result //= arr[idx+1]
	return result 
		
def solution(arr,oper):
	N = len(arr)
	answer = []
	min_num = 1000000000
	max_num = -1000000000

	op_list = [ '+' for _ in range( oper[0] ) ]
	op_list.extend( list('-' for _ in range(oper[1])))
	op_list.extend( list( '*' for _ in range(oper[2])))
	op_list.extend( list('//' for _ in range(oper[3])))

	#op_list에서 나올 수 있는 경우의 수대로 값을 구하기 
	for op in set(permutations(op_list, N-1)):
		tmp = caculate_num(arr,op)
		min_num = min(tmp,min_num)
		max_num = max(tmp,max_num) 
			
	answer.append(max_num)
	answer.append(min_num)
	return answer

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split(" ")))
	oper = list(map(int,input().split(" ")))

	answer = solution(arr,oper)
	for x in answer:
		print(x)

