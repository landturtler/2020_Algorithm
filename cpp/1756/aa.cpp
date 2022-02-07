//마지막 반죽의 깊이(얼마나 들어갔냐)

#include<iostream>
#include<algorithm>
#define MAX 300001
using namespace std;

int main() {	
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int N,D;
	long long pizzas[MAX],oven[MAX]; //반죽들의 지름을 순서대로 저장 
	cin >> D >> N; 
	
	//입력받음 
	long long tmp;
	oven[0] = 1000000001;
	for (int i =1;i<=D;i++) {
		cin >> tmp;  
		oven[i] = min(tmp,oven[i-1]);
	}		
	for(int i=0;i<N;i++)
		cin >> pizzas[i];
	reverse(oven+1,oven+D+1);

	int idx= 0;
	for(int i=0;i<N;i++) {
		int pizza = pizzas[i];
		//만약 전 도우보다 지름이 작으면 직전 도우 바로 위로 올라감 
		if( i > 0 && pizza <= pizzas[i-1] ) {
	//		cout <<"idx = "<<idx-1<<endl;
			if(++idx > D) break;
			continue;
		}
		//현재 반죽보다 지름이 작은 오븐의 가장 위쪽 위치 -1
//
	idx = (int)(lower_bound(oven+(idx+1),oven+D+1,pizza)- oven);
	/*
	else {
		for(int j = idx-1; j >0; j--) {
			if(oven[j] >= pizza)	{
			idx = j;
		
	//		cout <<"idx = "<<idx<<endl;
			break;
			}
		}
	}
	*/
	//idx = id - oven;
	if(idx > D ) break;
	}
	idx > D ? D+1 : idx;
	cout <<D-idx+1<<endl;
	return 0; 
}
