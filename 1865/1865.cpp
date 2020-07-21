/*
	웜홀 통한 사이클이 있는지 확인하는 문제 

*/

#include<iostream>
#include<vector>
using namespace std;
vector<vector<pair<int,int> >v;
int visited[500][500];
int sum[500][500]; //가중치의 합을 저장


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T,N,M,W;
	cin >> T;
	while(T--) {
	 	v.clear();
		fill(&visited[0][0],&visited[499][500],-1);

		cin >>N >> M >> W;
		for(int i=0;i<M;i++) {
			int a,b,ti;
			cin >> a >> b >> ti;
			v[a].push_back({b,ti});
			v[b].push_back({a,ti});
		}
	

	}



}
