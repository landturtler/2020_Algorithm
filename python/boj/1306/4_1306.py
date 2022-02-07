#그냥 print(answer, end = " ") 이랑 for x in answer: print(x, end = " ")랑 다름?
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))
box = deque(arr[:2 * M - 1]) 
max_box = max(box) 
answer = [str(max_box)]

for i in range(2 * M - 1, N):
    box.append(arr[i]) 
    bef_val = box.popleft() 
    #새로 들어온 값이 기존 max값보다 크면 update
    if arr[i] >= max_box:
        max_box = arr[i]
        
    elif bef_val == max_box: 
        max_box = max(box)
    answer.append(str(max_box))

print(answer, end = " ")
