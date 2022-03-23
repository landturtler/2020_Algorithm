'''
Programmers LV2
- 알고리즘 : 구현
- 소요시간 : 40분
- x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수를 구하라
- 처음 안 것 : 2진수 -> 10진수 : int(2진수값, 2) 
- 주의할 것 : 리스트 -> 문자열(''.join(arr))!!!!! (str(arr)로 하지 말 것), 16진수가 0x이고 2진수는 0b
'''
def solution(numbers):
    answer = []
    for num in numbers:
        bnum = list(bin(int(num))[2:])
        # 0이 있는 경우, 가장 작은 단위 0 ->1로 변경 후 그 오른쪽에 있는 1 -> 0 변경  
        if '0' in bnum:
            idx = ''.join(bnum).rfind('0')
            bnum[idx] = '1'
            if idx < (len(bnum) - 1):
                bnum[idx+1] = '0'
        
        # 0이 없는 경우, 기존의 가장 큰 자릿수 1 -> 0, 그 왼쪽 0-> 1
        else:
            bnum[0] = '0'
            bnum.insert(0,'1')
        #10진수로 바꿔서 저장 
        bnum.insert(0,'0b')
        answer.append(int(''.join(bnum),2))
    
    return answer
