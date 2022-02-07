#입력받기

N, M, K = list(map(int, input().split()))

array = list(map(int, input().split()))

count = 0

#내림차순 정렬 및 첫번째와 두번째로 큰 수 구하기 
array.sort(reverse = True)

first = array[0] #가장 큰 수 

second = array[1] #두번째로 큰 수 


#while문을 통해 첫번째 숫자부터 더함. 하나의 숫자는 연속해서 최대 k번가지 더할 수 있음

while M > 0:
 if M >= K: 
  count += ( K * first)
  M -= K
  if M == 0:
   break
  count += second
  M -= 1
 else:
  count += M * first
  M = 0

# 최대 합 출력 
print( count )





