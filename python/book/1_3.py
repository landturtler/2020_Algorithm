#범위 입력받기
N, M = map(int,input().split())
result = 0


#나는 처음에 2차원배열을 다 저장하고 그 후에 for문으로 비교하려 했는데,(2번 for문)
#for문 한번에 받으면서 최소값을 구할 수 있음
#N이 정수면 range를 써야하고 array면 안써도 됨 

for i in range(N):
 array = list( map(int,input().split()) )
 minvalue = min(array)
 result = max(result,minvalue)

print(result)
