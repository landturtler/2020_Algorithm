#include<iostream>
#include<vector>
#include<algorithm>
#define INF 987654321

using namespace std;


int go(int num, int col, vector<vector<int> > &color, vector<vector<int> > &v) {
	if(v[num][col] != INF) return v[num][col];
	if (num == 0 ) return 0; 
	v[num][col] = min(go(num-1,(col+1)%3,color,v),
	go(num-1,(col+2)%3,color,v)) + color[num][col];
	return v[num][col];
}

int solution(int n, vector<vector<int> > &color) {
	vector< vector<int> > v( n+1,vector<int>(3,INF));
	return min(min(go(n,0,color,v),go(n,1,color,v)),go(n,2,color,v));
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	int t;
	vector<vector<int>>color(n+1,vector<int>(3));
	for(int i=1;i<=n;i++) {
		for(int j=0;j<3;j++) {
			cin >>t;
			color[i][j] = t;
		}
	}
	cout <<solution(n,color)<<endl;
	return 0;
}
