/*
 나올 수 있는 경로는 총 4가지. 완전 탐색 수행  
 10개 수를 4개 그룹으로 그룹화(순열 만들기),단 각 말이 얻을 수 있는 최대 경로는 한정됨 
 map 
*/
#include<iostream>

using namespace std;

int dice[10];
vector< int > corner[3] = {{10,13,16,19,25,30,35,40,-1},{20,22,24,25,30,35,40,-1},{30,28,27,26,25,30,35,40,-1}};
vector< int > map = { 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,-1};
bool check[35]; //현재 해당 위치에 말이 있는지 check
int result;

void dfs(int cnt,int sum) {
	if( cnt == 10) {
		if( 

	}
	//각 말의 이동 경로 수행  
	for(int i=0;i<4;i++) {
		sel = i; //이번에 선택할 말 선택 	
	
	
	}

}

int main() {
	for(int i=0;i<10;i++)
		cin >> dice[i];
	//10개의 수를 4개 그룹으로 그룹화(순열 만들기)
   
  

}
