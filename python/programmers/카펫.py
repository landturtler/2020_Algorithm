'''
알고리즘 : 완전탐색
소요 시간 : 20분
'''
def solution(brown, yellow):
    answer = []
    for i in range(2, 2500):
        if (brown + yellow) % i == 0:
            j = (brown + yellow) // i
            if (i - 2) * (j - 2) == yellow:
                answer = [max(i, j), min(i, j)]
                break
    return answer
