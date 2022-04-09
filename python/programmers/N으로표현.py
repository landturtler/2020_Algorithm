'''
문제 : 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값
알고리즘 : DP
소요 시간 : 30분
오래걸렸던 부분 : dp의 매개변수를 number로 두고, dp[number] = number를 만들 수 있는 경우의 수로 접근해서 오래걸렸음 => set()을 사용해서 'dp[i] = N을 i번 사용해서 만들 수 있는 수들의 집합'으로 접근하기 
풀이 : 5를 2번 사용해서 만들 수 있는 수
    = 55(5를 이어붙임) + 10(5+5), 0(5-5), 25(5*5), 1(5/5)
    N을 n번 사용해서 만들 수 있는 수 :
    N을 n번 연달아서 사용할 수 있는 수 U
    N을 1번 사용했을 때 SET 과 n-1번 사용했을 때 SET을 사칙연산한 수들의 집합 U
    N을 2번 사용했을 때 SET 과 n-2번 사용했을 때 SET을 사칙연산한 수들의 집합 U
    N을 n-1번 사용했을 때 SET 과 1번 사용했을 때 SET을 사칙연산한 수들의 집합  
처음 안 것 : NNN 만드는 법 : int(str(N) * 3)
            set()을 순회하는 도중 사이즈가 바뀌면 에러남!!!!!
            순회전용 set()생성해서 순회가 끝나면 해당 set을 반영하는 식으로 변경 
'''

def solution(N, number):  
    if N == number:
        return 1
    
    #dp[i] = N을 i번 사용해서 만들 수 있는 수를 저장하는 set
    dp = []
    dp.append(set()) # dp[0] 채움 
    
    for i in range(1, 9): #i = 1 ~ 8
        number_set = set()
        number_set.add(int(str(N) * i))
        
        for j in range(1,i): #j = 1 ~ i-1
            for op1 in dp[j]:
                for op2 in dp[i-j]:# i-j : 
                    number_set.add(op1 + op2)
                    number_set.add(op1 - op2)
                    number_set.add(op1 * op2)
                    if op2 != 0:
                        number_set.add(op1 // op2)
        if number in number_set: 
            return i
        
        dp.append(number_set)
        
    return -1
