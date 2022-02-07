#왕실의 나이트
#수평 두 칸 이동 후 수직 한 칸 or 수직 두 칸 이동 후 수평 한 칸
#이동 가능한 경우의 수 : 8

input_data = input()
a = int(ord(input_data[0])) - int(ord('a')) + 1
h = int(input_data[1])
count = 0


dx = [0,1,0,-1]
dy = [-1,0,1,0]

#i는 두 번 이동할 방향
for i in range(4):
	j1 = (i+1+4) % 4
	j2 = (i-1+4) % 4

	nx1= a + dx[i] + dx[j1]
	ny1= h + dy[i] + dy[j1]

	nx2= a + dx[i] + dx[j2]
	ny2= h + dy[i] + dy[j2]

	if nx1 >= 1 and nx1 <= 8 and ny1 >= 1 and ny1 <= 8:
		count += 1
	
	if nx2 >=1 and nx2 <= 8 and ny2 >= 1 and ny2 <= 8:
		count += 1

print(count)


	
	
