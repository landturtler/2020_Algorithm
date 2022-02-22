'''
programmers Lv3
알고리즘 : 구현 (문자열) / 투포인터
처음안 것: float 연산 시, round()함수 사용해야 오차 안남(파이썬은 부동소수점 방식으로 표현하는데 부동소수점은 실수를 정확히 표현할 수 없는 문제 있음) // 혹은 decimal.Decimal()사용 
소요 시간 : 2시간 33분 (ㅠㅠ)
'''

## 이중for문 
def solution(lines):
    answer = 1
    times = []

    # 1. 데이터 정제 : 2016-09-15 / 's' 제거 후, 처리 시작시간과 끝시간을 각각 구함. 초 단위로 변경
    for line in lines:
        S,T = line[11:-1].split()
        end_time = round(int(S[:2]) * 3600 + int(S[3:5]) * 60 + float(S[6:]),3)
        start_time = round(end_time - float(T) + 0.001,3)
        times.append([start_time,end_time])   
    times.sort()
    
    # 2. times를 돌면서 1초 간 최대 처리량 탐색
    for i in range(len(times)):
        tmp = 1
        for j in range(0, i):
            if round(times[i][0] - 0.999, 3) <= times[j][1]:
                tmp += 1
        answer = max(answer, tmp)    
    
    return answer
    
    
## 투포인터
def solution(lines):
    answer = 1
    st_times = []
    ed_times = []

    # 1. 데이터 정제 : 2016-09-15 / 's' 제거 후, 처리 시작시간과 끝시간을 각각 구함. 초 단위로 변경
    # 2. 시작 시간과 종료 시간을 분리해서 저장 후 정렬
    for line in lines:
        S,T = line[11:-1].split()
        end_time = round(int(S[:2]) * 3600 + int(S[3:5]) * 60 + float(S[6:]), 3)
        start_time = round(end_time - float(T) + 0.001, 3)
        st_times.append(start_time)
        ed_times.append(end_time)

    st_times.sort()
    ed_times.sort()
    
    # 3. st_times를 돌면서 st_time - 1 + 0.001초 이후에 끝나는 종료 시간(ed_times[l_idx]) 탐색 : 투 포인터 
    #   - l_idx 이전의 ed_times 값들은 st_time -1 + 0.001초 이전에 끝나기 때문에(1초 간 겹치지 않기 때문에) 앞으로의 탐색에서도 카운팅할 필요 없음
    l_idx = 0
    for r_idx in range(1, len(st_times)):
        while (l_idx < r_idx and ed_times[l_idx] < round((st_times[r_idx] - 0.999), 3)):
            l_idx += 1      
        answer = max(answer, r_idx - l_idx + 1)    
    
    return answer
