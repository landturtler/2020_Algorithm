#입력받기

N, M, B = map(int, input().split())

board = [ 0 for _ in range(N) ]

second = 10000000
height = 0
sum_height = 0 #전체 높이의 합

for i in range(N):
	board[i] = list(map(int,input().split()))
	sum_height += sum(board[i])

#가능한 높이값들을 저장
height_set = set()
min_height = 0
max_height = sum_height // (M * N)

for i in range(max_height+1): #첨엔 min~max로 했었음 
	height_set.add(i)

height_list = list(height_set) #중복제거를 위해 set으로 입력받은 후 ,list로 변경

#가능한 높이값들로 평탄화 시키기 위해 걸리는 시간 측정
for h in height_list:
	basket = B #인벤토리 내 값 개수
	sec = 0 

	for i in range(N):
		for j in range(M):
			if board[i][j] == h:
				continue
			elif board[i][j] > h:
				basket += 1
				sec +=2
			else:
				basket -= 1
				sec += 1
	
	#인벤토리 내 개수가 음수개면 불가능한 경우로 판단
	if basket < 0:
		continue
	elif sec < second:
		second = sec
		height = h

print(second,height)






