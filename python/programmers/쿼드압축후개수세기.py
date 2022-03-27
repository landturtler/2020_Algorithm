'''
Programmers LV2 쿼드압축 후 개수 세기
- 알고리즘 : 분할정복
- 처음안 것 : 2차원 리스트 -> 1차원으로 바꾸는 법 : sum(arr,[])
              from Collections Counter : 1차원 리스트에서 각 원소의 개수를 map형식으로 저장해줌 
'''
arr_list = []
def func(arr,x,y,size):
    global arr_list
    N = len(arr)
    if size == 1:
        arr_list.append(arr[x][y])
    
    #압축 가능한지 판단
    else:
        check = True
        num = arr[x][y]
        for i in range(x,x + size):
            for j in range(y, y + size):
                if arr[i][j] != num:
                    check = False
                    break

        if check == True:
            arr_list.append(arr[x][y])

        else:
            n_size = size // 2
            func(arr,x,y,n_size)
            func(arr,x,min(N-1,y+n_size),n_size)
            func(arr,min(N-1,x+n_size),y,n_size)
            func(arr,min(N-1,x+n_size),min(N-1,y+n_size),n_size)
    
def solution(arr):
    answer = []
    func(arr,0,0,len(arr))
    answer.append(arr_list.count(0))
    answer.append(arr_list.count(1))
    return answer
