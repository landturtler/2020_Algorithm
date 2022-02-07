#8911 거북이
#F:앞, B:뒤, L:왼쪽으로 90도 회전, R: 오른쪽으로 90도 회전
#컨트롤 프로그램 명령어들을 입력받았을 떄, 겁구이가 이동한 영역을 모두 포함할 수 있는 가장 작은 직사각형 넓이를 구하라.
import sys
input = sys.stdin.readline

dx = [-1,0,1,0] #북,동,남,서 
dy = [0,1,0,-1]
dl = [3,2,1,0] #좌측으로 회전 
dr = [0,1,2,3] #우측으로 회전 

if __name__ == "__main__":
	T = int(input())
	for _ in range(T):
		commands = input() #명령어

		min_x,min_y,max_x,max_y = 0,0,0,0 #직사각형의 양 꼭지점
		x,y,d = 0,0,0 #최초 위치 / 방향

		for cmd in commands:
			if cmd == "L":
				d += 3
			elif cmd == "R":
				d += 1
			elif cmd == "F":
				x += dx[d%4]
				y += dy[d%4]
			elif cmd == "B":
				x -= dx[d%4]
				y -= dy[d%4]

			#직사각형 꼭지점 갱신
			min_x = min(min_x,x)
			max_x = max(max_x,x)
			min_y = min(min_y,y)
			max_y = max(max_y,y)

		print(abs(max_x - min_x) * abs(max_y - min_y))
	
