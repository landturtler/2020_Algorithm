/*
영식이의 비율을 얻으면 
-> 민식이의 비율도 알 수 있다.(1-영식 비율)
-> 분모는 공통이므로 분자를 기준으로 계산해보자.
-> 둘 중 짝수인 수를 기준으로 나누기
-> 수를 1,2,4,..8 등 2의 배수들의 합으로 나누기 
-----------------------
b :2^k -1, k는 1,2,4,8 등 합을 이루는 수들의 개수를 의미한다.

*/

#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;

long long yo,mi;//영식과 민식 비율의 분자
vector<char>pattern(63,'#'); 

void go(long long num,char c) {
	int idx = (int)floor(log2(num)); // num 이하의 2의 제곱수 찾기
	
	//0이 될 때까지 2의 제곱수들의 합으로 구함 
	while( num && idx >= 0 ) {
		if(pattern[idx] == '#'){
			pattern[idx] = c;
			num -= pow(2,idx);
		}
		//이미 해당 수가 선택되었으면 
		else idx--;
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	//영식 & 민식 비율 구하기 
	long long a,b;
	cin>>a>>b;
	int cnt=1;
    //분수 형식 맞추기 
 	if(log2(b+1)- (int)log2(b+1) !=0 ) {	
		while( cnt <=64 ) {
			cnt++;
			if(log2(cnt*b+1)- (int)(log2(cnt*b+1)) == 0)  //정수 판별 
			break;
		}
	}
	if(cnt > 64 ) {
		cout<<-1;
		return 0;
	}
	yo = a*cnt;
	mi = (b-a)*cnt;
	//cout<<"yo = "<<yo <<"mi = "<<mi;
	int k = log2(cnt*b+1);
	//cout<< "K = "<<k<<endl;
	//큰 수부터 채우기 
	if(yo > mi) {
		go(yo,'*');
		go(mi,'-');
	}
	else {
		go(mi,'-');
		go(yo,'*');
	}
	for(int i=k-1;i>=0;i--) {
		cout<<pattern[i];
	}
	return 0;
}
