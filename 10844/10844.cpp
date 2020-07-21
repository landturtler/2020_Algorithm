/*
10844
DP
N자리이고, 마지막 수가 k인 계단 수: N-1자리이고 마지막 수가 k-1 & k+1인 경우의 합(1,9제외)
*/
#include<iostream>
#include<cstring>
#define MAX 1000000000
using namespace std;
long long dp[101][10]; //dp[i][j] = i자리수 중 마지막 숫자가 j인 수들 중에서 계단 수의 개수

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	long long cnt = 0;
	cin >> N;
	memset(dp,0,sizeof(dp));
	
	for (int i = 1; i <= 9; i++) {
		dp[1][i] = 1;
	}

	for (int i = 2; i <= N; i++) {
		for (int j = 1; j <= 8; j++) {
			dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1];
			dp[i][j] = dp[i][j] % MAX;
		}
		dp[i][0] = dp[i - 1][1];
		dp[i][9] = dp[i - 1][8];
	}
	
	for (int i = 0; i <= 9; i++) {
		cnt += dp[N][i];
	}

	cnt = cnt % MAX;
	cout << cnt;
	return 0;
}