'''
문제 : 보석 이름 리스트가 주어질 때, 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 리턴
알고리즘 : 투포인터
처음 안 것: 투포인터를 쓰더라도 슬라이딩 윈도우 사용 시, 객체 k개를 조회해야하므로 시간복잡도가 O(k)가 되므로 시간 초과 날 수 있음
          -> 슬라이딩 윈도우 안쓰면서 투 포인트 쓰는 방식에도 익숙해 지자(반복문 한번 돌때 ed_idx++를 하거나 st_idx--)
헷갈렸던 것 : ed_idx++ 후 딕셔너리에 넣는 거랑 ed_idx값을 딕셔너리에 넣은 후 idx++하는 거랑 답이 다르게 나옴
            후자로 하면 맨 마지막에 st_idx-- 을 수행하는 while문 조건을 한 번 못 돈다
소요 시간 : 2시간 30분 (카카오 해설 참고)
'''
from collections import defaultdict

def solution(gems):
    answer = [1, len(gems)]
    N = len(set(gems)) #전체 보석 종류의 개수
    st_idx = 0
    ed_idx = 0
    gem_dict = defaultdict(int) #st~ed 범위에서 각 보석의 빈도수를 저장하는 딕셔너리
    gem_dict[gems[0]] += 1 #gems[0]값 넣고 while문 탐색 시작 
    
    while (st_idx < len(gems) and ed_idx < len(gems)):
        # 모든 보석이 안모였다면, ed_idx++ 후 gems[ed_idx] 보석 정보를 딕셔너리에 넣음
        if len(gem_dict) < N:
            ed_idx += 1
            if ed_idx == len(gems):
                break
            gem_dict[gems[ed_idx]] += 1
                      
        # 모든 보석 종류가 딕셔너리에 들어있을 경우, 더 짧은 범위로 갱신 후 보석 딕셔너리에 gems[st_idx]값을 하나 빼고 st_idx--
        else:
            if (ed_idx - st_idx) < (answer[1] - answer[0]):
                answer = [st_idx+1, ed_idx+1]
            
            if gem_dict[gems[st_idx]] == 1:
                del gem_dict[gems[st_idx]]
            else:
                gem_dict[gems[st_idx]] -= 1
            st_idx += 1
                   
    return answer
