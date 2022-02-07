/*
11052
DP
DP[i] : i개 카드를 살 수 있는 최대 금액
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
    
	vector<int> p(N+1, 0); //카드팩
	vector<int> dp(N+1, 0);
    
	for(int i=1;i<=N;i++)
	 	cin >> p[i];
	
	for(int i=1;i<=N;i++) // 이번에 선택할 카드 팩의 index. 해당 카드 팩을 구매하면서 만들 수 있는 금액의 경우의 수 구하기
	 	for(int j=0;j<=N-i;j++) 
		 	dp[i+j] = max(dp[i+j], dp[j] + p[i]);

	cout << dp[N] << endl;
    
	return 0;
}

