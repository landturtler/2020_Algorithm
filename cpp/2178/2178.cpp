/*
2178 미로탐색
문제:N*M크기 배열이 주어질 때 (1,1)에서 (N,M)까지 지나는 최소 칸 수를 구하라 
알고리즘 :bfs
*/

#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#define MAX 101
#define INF 987654321
using namespace std;

pair<int,int> d[4] = {{-1,0},{0,1},{1,0},{0,-1}};
string map[MAX];
int dis[MAX][MAX];
int N,M;

void bfs() { 
	queue<pair <int,int> > q;
	q.push(make_pair(0,0));
	dis[0][0] = 1;
	while(!q.empty()) {
		int cx = q.front().first;
		int cy = q.front().second;
		q.pop();
		for(int i=0;i<4;i++) {
			int nx = cx + d[i].first;
			int ny = cy + d[i].second;
			if(nx <0 || nx >= N|| ny <0 || ny >=M || map[nx][ny] == '0') continue;
			if(dis[nx][ny] > (dis[cx][cy]+1)) {
				q.push(make_pair(nx,ny));
				dis[nx][ny] = dis[cx][cy]+1;
			}
		}			
	}
}


int main() {
	ios_base::sync_with_stdio(false);
    fill(&dis[0][0],&dis[MAX-1][MAX],INF);
	cin.tie(0);
	
	cin>>N>>M;
	for(int i=0;i<N;i++) {
		cin>>map[i];
	}
	
	bfs();
	cout<<dis[N-1][M-1]<<"\n";
    return 0;
}