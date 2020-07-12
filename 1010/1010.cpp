#include<iostream>
#include<vector>
using namespace std;

//dp로 풀 때(bottom-up)
int solution(int n,int m) {
	vector<vector<int>> v(n+1,vector<int>(m+1,0));
	for(int i=1;i<=m;i++)	
		v[1][i] = i;
	
	for(int i=2;i<=n;i++) {
		for(int j=i;j<=m;j++) {
			if(j == i) {
				v[i][j] = 1;
				continue;
				}
			 for(int k=i-1; k<=j-1;k++) 
				v[i][j] += v[i-1][k];
		}
	}

	return v[n][m];
}

//조합으로 풀 때 

int go(int m, int n, vector<vector<int> > &v) {
	if( n == 0 || m == n ) return 1;
	if( v[m][n]) return v[m][n];
	return v[m][n] = go(m-1,n-1,v) + go(m-1,n,v);
}
int solution_2(int n,int m) {
	vector<vector<int> > v(n,vector<int>(m,0));
	return go(m,n,v);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
	int n,m,T;
	cin >> T;
	while(T--) {
	cin >> n >> m;
	cout <<solution(n,m)<<"\n";
	}
	return 0;
}
