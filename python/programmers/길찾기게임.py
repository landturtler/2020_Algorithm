'''
Programmers Lv3
문제 : 이진트리의 전위/ 후위 순회한 결과를 2차원 배열에 담아 출력하라
알고리즘 : 구현(이진트리 / 순회)
구현 시간 : 1시간 35분
헷갈렸던 것 : sort시 key = lambda : x(), list(~~).sort()로 list생성과 sort()를 한번에 하면 아무값도 저장 안됨
'''
import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data, pos, left = None, right = None):
        self.data = data # index
        self.pos = pos
        self.left = left # left 자식노드
        self.right = right # 

preorder_list = []
postorder_list = []

def order(node):
    preorder_list.append(node.data)
    if node.left:
        order(node.left)
    if node.right:
        order(node.right)
    postorder_list.append(node.data)

def solution(nodeinfo):
    answer = []
    # 노드값을 idx로 구하여 좌표값과 함께 nodes 리스트에 저장 + level 순으로 정렬
    nodes = sorted(list(info + [idx+1] for idx, info in enumerate(nodeinfo)), key = lambda x :(-x[1],x[0])) 
    
    # 이진 트리 생성 
    root = None
    for node in nodes:
        # root노드가 없으면 루트 노드 생성
        if root == None:
            root = Tree(node[2], node[:2]) 
            
        # root부터 탐색 시작하며 x좌표로 비교한다. 
        else:
            cur = root
            while 1:
                if node[0] < cur.pos[0] :
                    if cur.left:
                        cur = cur.left 
                    else:
                        cur.left = Tree(node[2], node[:2])# 노드 자리 찾음
                        break
                elif node[0] > cur.pos[0]:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Tree(node[2], node[:2]) # 노드 자리 찾음
                        break
                        
    order(root)
    answer = [preorder_list, postorder_list]
    
    return answer
