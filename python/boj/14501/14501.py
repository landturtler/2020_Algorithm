#맨 처음에 for문으로 돌리고 상담 가능한 날짜면 반드시 상담하도록 했는데, 그렇게 하면 모든 경우의 수가 안됨
#재귀 함수 형식으로 만들고, 상담 가능한 날짜여도 상담 할수도 , 안할수도 있게 하는게 좋은 것 같다.
#재귀 함수는 항상 리턴값이 있게 안만들어 도 됨! void로 만드는 연습 하기 

N = int(input())
answer = 0

def dfs(day,sum):
	if day > N:
		return
	elif day == N: #퇴사일일 경우 
		#마지막에 도달하고 나서 cnt값 비교해도 됨 
		global answer
		answer = max( answer, sum )
	
	else:
		#해당 날짜에 상담 건너 뜀 
		next_day = day + 1
		dfs(next_day,sum)

		#해당 날짜에 상담 함 
	
		sum += arr[day][1] #상담 비용 받기 
		next_day = day + arr[day][0] 
		dfs(next_day, sum)

#main 함수 
arr = []
for i in range(N):
	arr.append(tuple(map(int,input().split())))

dfs(0,0)



