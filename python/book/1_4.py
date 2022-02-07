#똑같이 값을 줄이는 건데, k로 나누는 게 더 빨리 걸림.
N, k = map(int,input().split())

count = 0

while( N > 1 ):
 count += ( N - (N // k) * k )#k의 배수가 될 때까지 빼야하는 수
 N =( N // k )#N을 k로 나눔 
 if N == 0:
  break
 else:
  count += 1

print(count)
  

