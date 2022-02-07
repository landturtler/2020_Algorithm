'''
5052 전화번호 목록
접근 방식1 : 트리
	그렇게 접근한 이유 -> 전화번호는 결국 수의 나열인데, 겹치는 부분이 있는지 확인하고 싶은 상황. 만약 부르트포스였다면 모든 전화번호를 탐색하면서 중복을 확인해야 하지만, 트리라면 한번의 탐색으로 알 수 있기 때문
	ex) abcd, abccc, abde가 있고 abc의 일관성을 추가로 검사하고 싶을 때, 전자라면 abcd와 abc 비교, abccc와 abc비교,abde와 abc비교  3번의 비교가 필요하다. 하지만 트리로 구현한다면, 트리의 abc까지만 탐색을 해보고 남은 d,cc에 대해서만 비교하기 때문에 탐색 횟수가 줄어들 수있다. 

	더 좋은 방법 -> 트라이 자료 구조(트라이의 가장 기본 문제가 해당 문제라고 한다.)
접근 방식 1-2: 트라이
	한 글자씩 노드를 타고 내려 가면서 그 다음 글자가 있는지를 확인하는 자료구조이며, 단어의 끝에 EndOfWord와 같은 boolean계수를 추가하면서 끝인지 아닌지를 판단할 수 있음

접근 방식2 : 해시맵 딕셔너리 
	그렇게 접근한 이유 -> 스스로 생각한 건 아니고 찾아보니 해시로도 풀 수 있었다. 사실상 브루트포스와 비슷하다고 생각 
	파이썬 딕셔너리가 해시 방식으로 구현되어 있기 딕셔너리를 정의해서 폰번호를 key로 하여 각 번호를 저장하고, 다른 전화번호를 비교하면서 딕셔너리에 존재하는지 비교한다.

접근 방식3 : 정렬 
	그렇게 접근한 이유 -> 한 전화번호가 다른 전화번호의 부분집합이면 일관성이 없는 것이므로 배열에 전화번호 목록들을 넣은 후 포함되어있는지를 검사. 하지만 시간 초과의 문제가 발생 가능

	그렇지만 정렬을 한다면 현재 문자열 기준으로 직후만 비교하면 된다. 따라서 string을 정렬 후 비교로 일관성 판단이 가능
'''

from sys import stdin
input = stdin.readline

# 트라이 
class Node(object):
	def __init__(self, key, data = None):
		self.key = key #단어의 글자 하나를 담는 곳
		self.data = data #마지막 글자인지 나타내는 flag
						#마지막 글자의 경우에 단어 전체를 data 필드에 저장 
		self.children = {} #dict

class Trie(object):
	def __init__(self):
		self.root = Node(None) 

	def insert(self,word):
		cur = self.root #루트부터 시작 
		
		for x in word:
			if x not in cur.children: #단어의 한 문자가 딕셔너리 자료형 cur의 자식에 없으면 
				cur.children[x] = Node(x)
			cur = cur.children[x] #cur의 위치를 하위 노드로 변경

		#마지막 글자이면 노드의 data필드에 문자열 전체 저장
		cur.data = word

	def search(self, word):
		cur = self.root #루트부터 시작 
		for c in word:
			if c in cur.children:
				cur = cur.children[c] #cur 업데이트 

				if cur.data is not None:
					return True
			else:
				return self.insert(word)

		return True 


def solve_tree(N, phone_number):
	tree = Trie()
	boolean = True

	for i in range(N):
		number = phone_number[i]

		if tree.search(number):
			boolean = False
			break
	
	if boolean:
		return("YES")
	else:
		return("NO")


# 해시함수
def solve_hash(N,phone_number):
	dic = {}
	flag = True
	#폰번호를 저장 
	for number in phone_number:
		dic[number] = 1
	
	for number in phone_number:
		tmp = ""
		for ch in number:
			tmp += ch #폰번호를 한글자씩 쪼개서 붙임
			if tmp in dic and tmp != number:
				flag = False
				break
	
	if flag:
		return("YES")
	else:
		return("NO")


# 정렬 
def solve_sort(N,phone_number):
	phone_number.sort(key=str)
	flag = True
	for i in range(N-1):
		if phone_number[i] == phone_number[i+1][:len(phone_number[i])]:
			flag = False
			break

	if flag:
		return("YES")
	else:
		return("NO")


if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		phone_number = list( input().rstrip() for _ in range(N))
		result = solve_hash(N,phone_number)
		print(result)


