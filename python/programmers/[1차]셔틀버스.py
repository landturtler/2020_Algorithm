'''
문제풀이 : 셔틀을 타고 사무실로 갈 수 있는 가장 늦은 도착시간(대기열의 가장 마지막에 섬)
알고리즘 : 리스트 / 정렬 
처음안 것 :zfill() 문자열 앞에 0 붙이기
'''
from bisect import bisect_right, bisect_left

def solution(n, t, m, timetable):
    answer = 0
    timetable.sort()
    crews = []
    
    # 0. 분 단위로 변경
    for x in timetable:
        hour, minute = x.split(':')
        crews.append(int(hour) * 60 + int(minute))
    
    # 1. 데이터 정제 : 마지막 셔틀 이후 대기열에 서는 크루 제거
    last_time = 9 * 60 + (n-1) * t # 가장 마지막 셔틀 시간 
    last_index = bisect_right(crews,last_time)
    crews = crews[:last_index]
    
    # 2. 셔틀 별 탈 수 있는 크루 정보를 담는 리스트 생성
    bus_list = [] #버스 별 탈 수 있는 크루의 대기 시간을 저장하는 리스트
    time_list = [ 9*60 + i * t for i in range(n)] #버스의 출발 시간 
    
    for time in time_list:
        last_crew = min(bisect_left(crews,time+1),m) #time시 버스에 마지막으로 탈 수 있는 크루의 대기 시간
        bus_list.append(list(crews[:last_crew]))
        crews = crews[last_crew:]
    
    # 3. case에 따라 결과 출력
    # 3-1. 가장 마지막 버스에 탄 승객 수가 m보다 작은 경우 : 마지막 버스 출발시간에 대기한다.
    if len(bus_list[n-1]) < m:
        answer = 9 * 60 + (n-1) * t
    # 3-2. 가장 마지막에 탄 크루의 대기시간보다 1분 전에 도착한다. 
    else:
        answer = bus_list[n-1][-1] - 1
        
    # 4. 분 단위 결과를 시:분으로 나눔
    answer = str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)
    return answer 
