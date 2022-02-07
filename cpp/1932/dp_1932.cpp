#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;


int go(int n,int j,vector<vector<int> > &tri,vector<vector<int> > v) {
	if( n == 0 ||j == 0 || j > n ) return 0;
	if( v[n][j] != -1) return v[n][j];
	v[n][j] = tri[n][j] + max(go(n-1,j-1,tri,v),go(n-1,j,tri,v));
	//cout <<"v["<<n<<"]["<<j<<"] = "<<v[n][j]<<endl;
	return v[n][j];
}

int solution(int n, vector<vector<int> > &tri) {	
	vector<vector<int> > v(n+1,vector<int>(n+1,-1));//해당 레벨까지 가는데 최대 값
	v[1][1] = tri[1][1];
	int ret = -1;
	for(int i=1 ; i <=n;i++) {
		//cout <<endl<<n<<","<<i<<" 경로 구하기 시작"<<endl;
		ret = max(ret, go(n,i,tri,v));

		}
	return ret;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);

	int n,tmp;
	cin >> n;
	vector<vector<int> > tri(n+1,vector<int>(n+1,-1));
	for(int i=1;i<=n;i++) {
		for(int j=1;j<=i;j++) {
			cin >> tri[i][j];
		}
	}
	cout << solution(n,tri);
	return 0;
	
	}
