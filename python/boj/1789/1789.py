#1789 수들의 합
#서로다른 N개의 합을 S라 할때, S가 주어지면 구할 수 잇는 N의 최댓값은 ?
# 처음에는 연속된 합을 구하는 거라 생각하고 투포인터를 생각했는데, 항상 연속된 합이 최대가 되는 건 아닌 것 같다. 

import math

answer = 0
S = int(input())
num = 0
cnt = 1

while num < S:
	num += cnt
	cnt += 1

if num == S:
	answer = cnt -1

else: #num > S인 경우
	answer = cnt - 2

print(answer)

