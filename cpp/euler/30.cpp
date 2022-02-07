#include<iostream>
#include<cmath>
#define MAX 
using namespace std;

int po[10];
int main() {
 	long long answer =0;

	for(int i=0;i<=9;i++) 
		po[i] = (int)pow(i,5);

	for(int i=2;i<400000;i++) {
		int getSum =0;
		int num = i;
		while(num) {
			getSum += po[num%10];
			num /= 10;
		}
		if(i == getSum) answer +=i;
	}

	cout<<answer;
	return 0;
}
