/*
문제: 1로 만들기(1463) top-down
문제: X가 3의 배수면 ->3으로 나누고 2의 배수면 ->2로 나누고 1을 뺀다.
*/

#include<iostream>
#include<algorithm>
#include<vector>

#define INF 999999999

using namespace std;

vector<int> dp(1000001,INF);

int solution(int n) {
	if(dp[n] != INF) return dp[n];
	
	if(n == 1) return 0;
	if(n%3 == 0) dp[n] = min(dp[n],solution(n/3)+1);
	if(n%2 == 0) dp[n] = min(dp[n],solution(n/2)+1);
	dp[n] = min(dp[n],solution(n-1)+1);
	return dp[n];
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);
	
	int n;
	cin >> n;
	solution(n);
	cout << dp[n] << endl;
	return 0;	
}


