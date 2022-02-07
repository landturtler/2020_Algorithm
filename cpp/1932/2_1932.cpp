#include<iostream>
#include <algorithm>
#define MAX 501
using namespace std;

int dp[MAX][MAX]; //dp[n][j] : n번째 level의 j번째 노드까지 순회 했을 때 구할 수 있는 최대 합
int tri[MAX][MAX]; //정수 삼각형 

int go(int n,int j) {
	if( n == 0 || j == 0 || j > n ) return 0; //정수 삼각형 범위 벗어남 
	if( dp[n][j] != -1) return dp[n][j];
	dp[n][j] = tri[n][j] + max(go(n-1,j-1),go(n-1,j));//자신의 좌측, 우측 부모 노드 중 큰 값을 더함
	return dp[n][j];
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);
    
    fill(&dp[0][0],&dp[MAX-1][MAX],-1);
    fill(&tri[0][0],&tri[MAX-1][MAX],-1);
    
    int N,sum = -1;
    cin >> N;
	for(int i=1;i<=N;i++) {
		for(int j=1;j<=i;j++) {
			cin >> tri[i][j];
		}
	}

    dp[1][1] = tri[1][1];
    for(int i=1;i<=N;i++) 
        sum = max(sum,go(N,i));
    
    cout << sum;
	return 0;
}
