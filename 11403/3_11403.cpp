#include<iostream>
#include<cstring>
#define MAX 101
using namespace std;

int N;
bool map[MAX][MAX];
bool isLinked[MAX][MAX]; //방문 여부 출력과 동시에 두 정점 사이의 연결 여부를 알려주는 배열
bool visited[MAX][MAX];

void dfs(int start) {
	for (int i = 0; i < N; i++) {
	 	if(visited[start][i])
		 	continue;
		if (map[start][i] == 1) {
			isLinked[start][i] = 1;
			visited[start][i] = 1;
			dfs(i);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	memset(isLinked, 0, sizeof(isLinked));
	memset(visited, 0, sizeof(visited));

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		dfs(i);
		for(int j=0;j<N;j++)
		 	visited[i][j] 

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
		 	cout << isLinked[i][j] << " ";
		printf("\n");
	}
	return 0;
}

