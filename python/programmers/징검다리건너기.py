'''
Programmers Lv3
문제 : 매 징검다리를 건널 때마다 1씩 감소하고, 0부턴 해당 징검다리를 밟을 수 없다. 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k가 매개변수로 주어질 때, 최대 몇 명까지 징검다리를 건널 수 있는지?
알고리즘 : 이분탐색
배운 점 : input 범위가 크고 + 문제에서 나올 수 있는 최댓값과 최솟값을 유추할 수 있고(여기선 최댓값이 2억, 최솟값이 1) + 구하려고 하는 값이 ~최솟값(최댓값)을 구하는 경우, 이분탐색을 고려하자
         처음에 투포인터로 구하려 했는데, st_idx를 갱신할 때마다 바뀌는 범위에서의 최솟값을 또 구해야 하므로 결국 시간초과가 난다.
소요 시간 : 1시간 5분(이분탐색이라고 생각하기까지 시간이 걸렸다.)
'''
def solution(stones, k):
    answer = 0
    left = 0
    right = max(stones)

    while left <= right:
        # 건널 수 있는 니니즈 친구 수
        mid = (left + right) // 2
        
        # 연속한 k개 징검다리값 < mid 이면 mid만큼 건널 수 없다.
        flag = True
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt == k:
                    flag = False
                    break
            else:
                cnt = 0
                
        if flag == True:
            answer = max(answer,mid)
            left = mid + 1
        
        else:
            right = mid - 1
        
    return answer
