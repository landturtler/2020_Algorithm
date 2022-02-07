#꿀 아르바이트 
#각 날짜별로 받을 수 있는 금액이 다르고, 한번에 최대 m일밖에 연속으로 일을하지 못함
#벌 수 있는 최대 금액 출력하기

N,M = map(int,input().split())
answer = 0 
pays = list(map(int,input().split()))

for start_day in range(N-M+1):
	answer = max(answer,sum(pays[start_day:start_day+M]))

print(answer)
