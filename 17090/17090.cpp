#include<iostream>
#include<algorithm>
#define MAX 501
using namespace std;
int N,M,sum;
int arr[MAX][MAX],dp[MAX][MAX];
pair<int,int> d[4] = {{-1,0},{0,1},{1,0},{0,-1}};

//(i,j)가 탈출할 수 있는지 결정 
bool go(int i,int j) {
    //1.해당 좌표에 대한 값이 이미 저장되어있는지 혹은 최초로 탈출 성공한 곳인지 확인
	if( i < 0 || j< 0 || i >=N || j >= M) return true; //최초로 탈출성공
	else if(dp[i][j] != -1) return dp[i][j]; //해당 좌표에 이미 탈출 경로가 있으면 성공 

    //2.값이 저장되어있지 않으면 탐색 시작 
    dp[i][j]=0; //기본값을 false로 지정 후, 탈출 할 수 있는 곳 만나면 true로 바꿈
	int ni = i + d[arr[i][j]].first;
	int nj = j + d[arr[i][j]].second;
    dp[i][j] = go(ni,nj);
    
	return dp[i][j];
}

int main() {
	cin >> N >> M;
	char tmp;
	int sum=0;
	fill(&dp[0][0],&dp[MAX-1][MAX],-1);
	for(int i=0;i<N;i++) {
		for(int j=0;j<M;j++){
			cin >> tmp;
			if(tmp == 'U') arr[i][j] = 0;
			else if(tmp == 'R') arr[i][j] = 1;
			else if(tmp == 'D') arr[i][j] = 2;
			else arr[i][j] = 3;
		}
	}	
	for(int i=0;i<N;i++) {
		for(int j=0;j<M;j++) {
				if(go(i,j)) sum++;
		}
	}

	cout<<sum;
	return 0;
}
