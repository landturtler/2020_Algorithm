/*
11403
DFS
*/

#include<iostream>
#include<cstring>
#define MAX 101
using namespace std;

int N;
bool map[MAX][MAX];
int connect[MAX][MAX]; //방문 여부 출력과 동시에 두 정점 사이의 연결 여부를 알려주는 배열

// x->y로 갈 수 있는지 여부 출력
bool dfs(int x,int y) {
	 //이미 예전에 x->y 연결 여부를 확인한 적이 있으면 해당 값 리턴 
	if(connect[x][y] != -1) return connect[x][y];
	
	//x->y 경로 탐색 
	for (int i = 0; i <N; i++) {

	}
	return connect[x][y];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	memset(connect, -1, sizeof(connect));

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			if(map[i][j]) connect[i][j] = 1; 
		}
	}
	
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++)
			cout << dfs(i,j) << " ";
		cout<<endl;	
	}
	return 0;
}

///////////////////////////////////////////
/*
플로이드 와샬(최단 경로 알고리즘)
 dist[i][j] : i에서 j로 가는 최단 거리
 만약 i와 j 사이에 중간 정점 k가 있을 때
 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

*/
#include<iostream>
#include<cstring>
using namespace std;

int N;
bool map[101][101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	memset(map, 0, sizeof(map));

	cin >> N;
	for(int i=0;i<N;i++) {
		for(int j=0;j<N;j++){
			cin >> map[i][j];
		}
	}
	for(int x=0;x<10;x++){
		for(int i=0;i<N;i++){
		 	for(int j=0;j<N;j++){
			 	for(int k=0;k<N;k++){ //중간 정점 
				 	if(k!=i && k!=j) //i와 j가 연결되어 있거나, i와 k & k와 j가 연결되어 있으면 i->j 연결 가능
					 	map[i][j] = map[i][j] || (map[i][k] && map[k][j]);	
				}
			}
		}
	}

	for(int i=0;i<N;i++){
	 	for(int j=0;j<N;j++){
		 	cout << map[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
