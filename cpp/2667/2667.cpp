/*
	단지번호붙이기
	그래프, DFS, BFS
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 25
using namespace std;

string input;
int N;
bool town[MAX][MAX], visited[MAX][MAX];
vector<int> apartment; //각 단지 별 아파트 개수 저장
pair<int,int> d[4] = {{-1,0},{0,1},{1,0},{0,-1}};
 
int bfs(pair<int, int> cur){
	int cnt = 0;
	queue<pair<int, int>> q;
	q.push(cur);
	while(!q.empty()){
		cnt++;
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		
		for(int i=0;i<4;i++){
			int nx = x + d[i].first;
			int ny = y + d[i].second;
			if(nx<0 || nx==N || ny<0 || ny==N)    continue;
			if(town[nx][ny] && !visited[nx][ny]){
				visited[nx][ny] = true;
				q.push({nx, ny});
			}
		}
	}
	return cnt;
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
    int total=0;

	cin >> N;
    fill(&town[0][0],&town[MAX-1][MAX],0);
    fill(&visited[0][0],&visited[MAX-1][MAX],false);
	
	for(int i=0;i<N;i++){
		cin >> input;
		for(int j=0;j<N;j++){
			town[i][j] = (input[j]=='1'? true : false);
		}
	}
    
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(town[i][j] && !visited[i][j]){
				total++;
				visited[i][j] = true;
				apartment.push_back(bfs({i, j}));
			}
		}
	}
	cout << total << "\n";
	sort(apartment.begin(), apartment.end());
	for(auto x : apartment)
		cout << x << "\n";
}
