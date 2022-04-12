'''
문제 정리 : 내가 번 돈(부하한테 받은돈 포함)의 10%을 내 윗사람한테 떼준다.
자료 구조 : 트리?
로직 접근 방식 : 아래사람의 돈을 합쳐서 위로 보내야 하므로, 트리 탐색
알고리즘 접근 방식 : DP는 아님(봣던 걸 또 볼 필요는 없다.)
오래걸린점 : 부하에게 받은 돈을 모두 합한 후에 10%를 떼는 것이 잘못됨(개별적으로 떼야 하므로 순회가 아니고, 일반 탐색)
생각할 것 : 트리순회같은 문제에서 global변수를 쓰는것에 껄끄러워하지 않도록, 불만이면 클래스 만들어서 순회하기
소요시간 : 1시간
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
employees = defaultdict(str)
total_income = defaultdict(int)

def dfs(name, money):
    global employees, sell_info, total_income
    money_to_give = (money // 10)
    total_income[name] += (money - money_to_give)
    if employees[name] and money_to_give:
        dfs(employees[name], (money // 10))
        
def solution(enroll, referral, seller, amount):
    global employees, sell_info, total_income
    answer = []
    
    #1. 트리구조 만들기 (자식이 key, 부모가 value)
    for i in range(len(enroll)):
        employees[enroll[i]] = referral[i]
        
    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)
        #sell_info[seller[i]].append(amount[i] * 100)
    
    #3. 판매원 별 수입 출력
    for emp_name in enroll:
        answer.append(total_income[emp_name])
    
    return answer
