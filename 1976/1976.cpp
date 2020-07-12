/*
간선 정보가 들어있고, 여행 경로가 주어졌을 때, 해당 경로로 여행이 가능한지 여부를 판별하는 프로그램 작성 
*/

#include<iostream>
#define MAX 201
using namespace std;
int N,M;
bool map[MAX][MAX];//여행 지도 
int route[1000];
bool visited[MAX]; // 해당 여행지를 갈 수 있는지 

//st와 연결되어있는 곳 방문 탐색 진행 
void go(int st) {
	visited[st] = true;
	for(int i =0;i<N;i++) {
		if(!visited[i] && map[st][i])
			go(i);
	}
}

int main() {
	int route[1000]; //여행 계획 
	cin >> N >> M;

	//간선 정보 입력받음 
	for(int i =0;i<N;i++) {
		for(int j =0;j<N;j++)
			cin >> map[i][j];
	}
	//여행 계획 정보 입력받음 
	for(int i =0;i<M;i++) 
		cin >> route[i];

	//첫번째 여행지부터 탐색 시작 
	go(route[0]);
	

	//탐색 종료 후, 각 여행 경로에 해당하는 곳을 방문하지 못했으면 여행 불가 
	bool flag = true;
	for( int i=0;i<M;i++){
		if(!visited[route[i]])
			flag = false;
			break;
	}

	if(flag) cout <<"YES"<<endl;
	else cout <<"NO"<<endl;

	return 0;
	
}
