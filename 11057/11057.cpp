/*
11057
문제: 왼쪽->오른쪽으로 갈수록 오르막 수인 수를 오르막 수라 할 때, N자리 수 중 오르막 수의 개수?(0으로 시작 가능)
알고리즘 : DP
dp[i][j]: i자리수 중 끝자리가 j인 수 중 오름수 개수 = i-1자리 오름수들 중 끝자리가 0~j인 수들의 합
*/
#include<iostream>
#include<cstring>
#define DIV 10007
#define MAX 1001
using namespace std;
long long dp[MAX][10]; //dp[i][j] :i자리수 중 마지막 숫자가 j인 오르막 수의 개수

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	long long cnt = 0;
	cin >> N;
	memset(dp,0,sizeof(dp));
   
    //한자리 경우의 수 
	for (int i = 0; i <= 9; i++)
		dp[1][i] = 1;

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j <= 9; j++) { 
			for (int k = 0; k <= j; k++) { 
				dp[i][j] += dp[i-1][k];
				dp[i][j] %= DIV;
			}
		}
	}

	for (int i = 0; i <= 9; i++) {
		cnt += dp[N][i];
	}
	cnt %= DIV;
	cout << cnt;
	return 0;
}