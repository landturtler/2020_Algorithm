'''
Programmers Lv3
문제 : 이진트리의 전위/ 후위 순회한 결과를 2차원 배열에 담아 출력하라
알고리즘 : 구현(이진트리 / 순회)

'''
#def preorder()


#def postorder()

def solution(nodeinfo):
    answer = [[]]
    
    # 1. node의 x,y좌표 순서 바꾼 후 레벨(y좌표) 별로 정렬
    nodes = list([y,x] for x, y in nodeinfo)
    nodes.sort()

    return answer
