#실전문제 6.3
#성적이 낮은 순서로 학생 출력하기

N = int(input())
students = []

for i in range(N):
	input_data = input().split()
	students.append( [input_data[0],int(input_data[1])])

#키를 이용하여 점수 기준 정렬
students = sorted(students, key = lambda student :(student[1],student[0]))

for student in students:
	print(student[0], end = ' ')


