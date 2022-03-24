'''
Programmers Lv3
- 소요 시간 : 20분
- 알고리즘 : 정렬 / 투포인터
- 두 리스트를 정렬 후, B[idx_b] > A[idx_a]이면(B가 이기면) idx_a, idx_b를 둘 다 ++
  B[idx_b] <= A[idx_a]이면(B값이 A값보다 같거나 작으면) idx_b만 ++ 
'''
def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    idx_A = 0
    idx_B = 0
    while idx_B < len(B):
        if A[idx_A] < B[idx_B]:
            idx_A += 1
            idx_B += 1
            answer += 1
        else:
            idx_B += 1
    return answer
