#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

vector<vector<long long> > dp(31,(vector<long long>(31)));
long long solve(int one, int half) {
	if (one == 0) return 1;

	long long &ret = dp[one][half];
	if (ret != -1)	return ret;
	ret = 0;
	ret = solve(one - 1, half + 1);
	if (half > 0)
		ret += solve(one, half - 1);
	return ret;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); 
	cout.tie(NULL);
	int n;
	while(1) {
		fill(dp.begin(),dp.end(),vector<long long>(31,-1));
		cin >> n;
		if(n == 0) break;
		long long ret = solve(n,0);
		cout<<ret<<"\n";
	}
	return 0;
}
