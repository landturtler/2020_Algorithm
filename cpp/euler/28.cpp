/*
1001 * 1001 이므로, 정사각형은 1001/2개(1 제외)
1, (3,5,7,9)  (13,17,21,25)  (31,37,43,49)...
 +2         +4             +6 
space = 수 차이
num = 모서리 숫자
*/
#include<iostream>
using namespace std;

int main() {
	int answer = 1;
	int space = 0;
	int num = 1;

	for(int i= 1;i<=500;i++) {
	 	space += 2;
		for(int j=0;j<4;j++) {
			num +=space;
			answer += num;
		}
	}
	cout<<answer;
	return 0;
}
