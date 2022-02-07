/*
1. 제곱근들을 저장한다. 

*/

#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	long long min,max;
	bool p[1000001]; //p[i] = true이면 min+idx가 제곱수의 배수 
	memset(p,false,sizeof(p));

	cin >> min >> max;
	int cnt = max - min + 1 ;//제곱 ㄴㄴ 수의 개수 
	int maxSq = (int)sqrt(max);//max(이하)의 제곱근 

 //1. 제곱수 생성 후, 제곱수의 배수 중 최초로 min이상 값 찾기 
	for(long long i = 2;i<=maxSq;i++) {
		long long powNum = i*i; //제곱수 생성 
		long long start = min/powNum * powNum; //sqr배수 중 처음으로 min보다 큰 값 

//2.제곱수에 의해 나누어 지는 수들을 true로 check
		for( long long num = start; num <= max; num += powNum) //제곱수의 배수를 true로
		 	p[(int)num-min] = true;
	}

//3. 제곱 ㄴㄴ수 구하기 
	for(int i = 0; i<max-min+1;i++)
		if(p[i])cnt--;
	
	cout<<cnt<<"\n";
	return 0;

}
