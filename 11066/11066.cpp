/*
여러 파일을 합쳐 최종적으로 하나의 파일을 만든다. 두 파일을 합친 임시파일의 크기는 두 파일의 크기 합일 때,
하나의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.
조건: 임시파일을 이루는 파일들은 번호가 연속이 되어야 한다.
for문으로 풀려면 각 case당 발생할 수 있는 경우의 수를 다 정리해야 하는데, 정리가 어렵다. 따라서 재귀로 풀 것
*/
#include<iostream>
#include<vector>
#define MAX 501
#define INF 987654321
using namespace std;
int sum[MAX]; //1~i까지 파일의 합 
int dp[MAX][MAX];
void print(int *sum) {
	for(int i=0;i<10;i++)
		cout<<sum[i]<<" ";
	cout<<endl;

}

int solution(int start,int end) {
	if(dp[start][end] != INF) return dp[start][end]; 
	else if (start == end )  return 0;

	for(int i= start; i< end;i++) {
		int getSum = solution(start,i) + solution(i+1,end) + sum[end]-sum[start-1];
		dp[start][end] = min(dp[start][end],getSum);		
	}
	return dp[start][end];
}

int main() {
	int T,K;
	cin >> T;
	while(T--) {
		cin >> K;
		fill(&dp[0][0],&dp[MAX-1][MAX],INF); //dp배열 초기화 
		fill(&sum[0],&sum[MAX],0);
		//sum배열 입력받음 
		cin >> sum[0];
		for(int i=1;i<K;i++) {
			cin >> sum[i];
			sum[i] += sum[i-1];
		}
		cout << solution(0,K-1) <<endl;
	}
	return 0;
}
