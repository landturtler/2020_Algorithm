'''
programmers Lv3
문제 : 응모자 아이디와, 불량 사용자 아이디 목록이 주어질 때 당첨에서 제외되어야 할 제재아이디 목록의 경우의 수
알고리즘 : 브루트포스
헷갈렸던 것 : 중복제거 위해 answer를 set으로 정의한 것. permutation쓸 때 list()붙이기
            permutations의 결과쌍은 튜플 형식으로 나옴
소요시간 : ing
'''

from itertools import permutations

def check(users, banned_id):
    #user[i]가 banned_id[i]에 포함되는지 확인
    for i in range(len(users)): 
        uid = users[i]
        bid = banned_id[i]

        # 길이가 다르면 무조건 false
        if len(uid) != len(bid):
            return False
        
        # 각 문자 비교
        for x in range(len(uid)):
            if bid[x] == '*':
                continue
            
            if uid[x] != bid[x]:
                return False     
    return True
        
def solution(user_id, banned_id):
    answer = set() #중복 제거
    user_comb = list(permutations(user_id, len(banned_id))) #banned_id와 매칭할 user-id 조합 리스트 생성
                    
    #user_id 조합이 banned_id에 포함되는지 확인
    for users in user_comb:
        if check(users,banned_id) == True:
            answer.add(users)   
                     
    return len(answer)
