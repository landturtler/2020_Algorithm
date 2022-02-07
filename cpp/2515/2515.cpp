#include<iostream>
#include<vector>
#include<algorithm>
#define MAX 300001
using namespace std;

int N,S;
vector<pair<int,int> >picture;
int dp[];// dp[i][j] = i번째 사진까지 보았을 때 구할 수 있는 최대 금액 

int getSum(int num,int sum ) {
	if(num < 0) return 0;
	else if(dp[num] != -1) return dp[num];
	
	if(num > 0 && picture[num].first - picture[num-1].second >= S)
	int re = 
	 dp[num] = max(dp[num-1], 
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	fill(&dp[0],&dp[MAX],-1);

	cin >> N >> S;

	for(int i=0;i<N;i++) {
		int h,p;
		cin >> h >> p;
		picture.push_back({h,p});
	}

	sort(picture.begin(),picture.end());
	
	cout<<getSum(N-1,0);
	return 0;
}
