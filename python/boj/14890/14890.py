## 14890 경사로 
import sys
input = sys.stdin.readline

def check(i,flag):
	##가로 탐색 
	if flag == 0:
		c = [ 0 for _ in range(N)] #경사로 설치 유무 
		for j in range(N-1):
			if abs(arr[i][j] - arr[i][j+1]) > 1:
				return 0
	
			##다음 위치가 더 높은 경우 
			elif arr[i][j] < arr[i][j+1]:
				##경사로를 놓을 수 있는지 판단
				for k in range(L):
					if j - k < 0 or arr[i][j-k] != arr[i][j] or c[j-k] == 1:
						return 0
				
				for k in range(L):
					c[j-k] = 1
			
			##이전 위치가 더 높은 경우
			elif arr[i][j] > arr[i][j+1]:
				for k in range(L):
					if (j+k+1) > N or arr[i][j+1] != arr[i][j+k+1] or c[j+1+k] == 1:
						return 0
				
				for k in range(L):
					c[j+1+k] = 1

		return 1

	##세로 탐색
	elif flag == 1:
		c = [ 0 for _ in range(N)] #경사로 설치 유무 
		for j in range(N-1):
			if abs(arr[j][i] - arr[j+1][i]) > 1:
				return 0
	
			##다음 위치가 더 높은 경우 
			elif arr[j][i] < arr[j+1][i]:
				##경사로를 놓을 수 있는지 판단
				for k in range(L):
					if j - k < 0 or arr[j-k][i] != arr[j][i] or c[j-k] == 1:
						return 0
				
				for k in range(L):
					c[j-k] = 1

			##이전 위치가 더 높은 경우
			elif arr[j][i] > arr[j+1][i]:
				for k in range(L):
					if (j+k+1) > N or arr[j+1][i] != arr[j+k+1][i] or c[j+1+k] == 1:
						return 0

				for k in range(L):
					c[j+1+k] = 1

		return 1	

if __name__ == "__main__":
	N, L = map(int,input().split())
	arr = [list(map(int,input().split())) for _ in range(N)]
	result = 0

	for i in range(N):
		result += check(i,0) ##가로 탐색 
		result += check(i,1) ##세로 탐색 

	print(result)
