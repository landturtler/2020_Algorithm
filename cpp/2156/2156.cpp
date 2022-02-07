#include<iostream>
#include<algorithm>
#define MAX 10001
using namespace std;
int dp[MAX][2],wine[MAX];
int N,sum;

int go(int num,int cnt) {
	if( num < 0 ) return 0;
	else if(dp[num][cnt] != -1) return dp[num][cnt];

	//dp 채우기(num번째 를 선택 하는 경우,안하는 경우
	if(cnt >0) dp[num][cnt] = go(num-1,cnt-1)+wine[num];
	else dp[num][cnt] = max({go(num-1,0),go(num-1,1),go(num-1,2)});
	
	//cout << "dp["<<num<<"]["<<cnt<<"]="<<dp[num][cnt]<<" ";
	return dp[num][cnt];
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	fill(&dp[0][0],&dp[MAX-1][2],-1);
	
	cin >> N;
	for(int i=0;i<N;i++)
		cin >> wine[i];

	sum = max({go(N-1,0),go(N-1,1),go(N-1,2)});
	cout<<sum;
		return 0;

}
