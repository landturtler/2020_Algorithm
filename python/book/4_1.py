#입력받기
N = int(input()) #배열 크기 

plans = list(input().split()) #여행 경로 

cur = [1,1]
                       
for i in range(len(plans)):
 if(plans[i] == 'L' and cur[1] > 1 ):
  cur[1] -= 1

 elif(plans[i] == 'R' and cur[1] <= N ):
   cur[1] += 1

 elif(plans[i] == 'U' and cur[0] > 1 ):
  cur[0] -= 1
 
 elif(plans[i] == 'D' and cur[0] <= N):
  cur[0] += 1

print(cur) 
