#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

pair<int, int > go(int n,vector<vector<int> > &tri,vector<pair<int,int> > v) {
	if( v[n].second != -1) return v[n];

	int bIdx = go(n-1,tri,v).first;
	v[n].first = (tri[n][bIdx] < tri[n][bIdx+1]) ? bIdx+1 : bIdx;
 	v[n].second = tri[n][v[n].first] + go(n-1,tri,v).second;
	cout <<"v["<<n<<"].first = "<<v[n].first <<", second = "<<v[n].second<<endl;
	return v[n];
}

int solution(int n, vector<vector<int> > &tri) {	
	vector<pair<int,int> > v(n+1,pair<int,int>({-1,-1}));//해당 레벨까지 가는데 최대 값
	v[1] = {1,tri[1][1]}; //index, 값 
	return go(n,tri,v).second;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);
	vector<vector<int> > tri(501,vector<int>(501,-1));

	int n,tmp;
	cin >> n;
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=i;j++) {
			cin >> tri[i][j];
		}
	}
	cout << solution(n,tri);
	return 0;
	
	}
