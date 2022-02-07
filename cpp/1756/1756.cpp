//마지막 반죽의 깊이(얼마나 들어갔냐)

#include<iostream>
#include<map>
#include<algorithm>

#define MAX 300001
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N,D;
	map<int,int> oven; // 오븐의 깊이가 key,지름이 value인 map
	int doughs[MAX]; //반죽들의 지름을 순서대로 저장 

	cin >> D >> N;
	int tmp;
	//오븐, 도우 입력값 받음 
	for (int i =1;i<=D;i++) {
		cin >> tmp;  
		oven.insert({i,tmp});
	}	
	oven.insert({D+1,MAX});
	
	for(int i=0;i<N;i++)
		cin >> doughs[i];
	
	//깊이 구하기 
	int idx= D+1; //직전 반죽의 위치 
	for(int i=0;i<N;i++) {
		bool flag = false;
		int dough = doughs[i];
		for(int j = idx-1;j > 0; j--) {
			if(dough > oven[j-1]->second && dough <= oven[j]->second) {
				idx = j;
				flag = true;
				break;
 			}	
		}
		if(!flag) {
			cout <<0<<endl;
			return 0;
		}
	}
	cout << idx<<endl;
	return 0; 
}
