#include<iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(NULL);
	cin.tie(0);
	int n, k;
	int coin[100],dp[10001] = {1,0,}; //dp[0] = 1 
	
	cin >> n >> k;
	
	for(int i=0;i<n;i++) cin >> coin[i];

	
	for(int i=0;i<n;i++) { 
		for(int j=1;j<=k;j++) {
			if(j - coin[i] >=0 )	dp[j] += dp[j-coin[i]];
		}
	}
 
	cout<<dp[k]<<endl;
	return 0;
}
