#2978 블랙잭
#카드 합이 M을 넘지 않으면서 M과 가장 가깝게 만들 수 있는 3장의 합
#정렬할가? 근데 굳이 할 필요는 없을 것 같음 


N, M = map(int,input().split())
cards = list(map(int,input().split()))
cards.sort()
answer = 0

#3가지 조합 직접 구현하기 
def dfs(cnt,max_index,sum):
	if sum > M:
		return
	elif cnt == 3:
		global answer
		answer = max( answer, sum )
	else:
		for i in range(max_index+1,N):
			dfs(cnt+1,i,sum+cards[i])
			dfs(cnt,i,sum)

dfs(0,-1,0)

print(answer)

	
		
	

