#include<iostream>
#include <vector>
using namespace std;

pair<int,int> fib(int n,vector<pair<int,int> > &v) {
	if(v[n].first != -1) return v[n];
	else {
		v[n].first = fib(n-1,v).first + fib(n-2,v).first;
		v[n].second = fib(n-1,v).second + fib(n-2,v).second;
		return v[n];
	}
}

void sol(int n) {
	vector<pair<int,int > > v(41,pair<int,int>({-1,-1}));
	v[0] = {1,0};
	v[1] = {0,1};
	pair<int,int> ret = fib(n,v);
	cout<<ret.first <<" "<<ret.second<<"\n";
	v.clear();
	return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
	int T,n;
	cin >> T;
	while(T--) {
		cin >> n;
		sol(n);
	}
	return 0;
}
