#include<iostream>

using namespace std;

long long solution(int n) {
	//avector<long long> dp(n+1);
	long long dp[31] ={0,};
	dp[0] = 1;
	dp[1] = 1;
	for(int i=2;i<=n;i++) {
		for(int j =0;j<i;j++)
			dp[i] += (dp[j]*dp[i-1-j]);
	}
	return dp[n];
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n;
	while(1) {
		cin >> n;
		if(n ==0) break;
		long long ret = solution(n);
		cout<<ret<<endl;
	}
	return 0;
}
