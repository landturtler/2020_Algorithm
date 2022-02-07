#include <iostream>
#define MAX 101
using namespace std;
int numbers[MAX];
long long dp[MAX][MAX]; // i,sum
int result,N;

//cnt번째 수를 계산하는 함수 
long long go(int cnt, int total ) {
	if(dp[cnt][total] != 0) return dp[cnt][total];
	if ( cnt == N-1) {
		if(total == result ) return 1;
		else return 0;
	}
	if( total +numbers[cnt] <=20 ) dp[cnt][total] += go(cnt+1,numbers[cnt]+total);
	if( total -numbers[cnt] >= 0 ) dp[cnt][total] += go(cnt+1,numbers[cnt]-total);
	return dp[cnt][total];
}

int main() {	
	cin >> N;
	for(int i=0;i<N;i++)
		cin >>numbers[i];
    fill(&dp[0][0],&dp[MAX-1][MAX],0);
	result = numbers[N-1];
	cout << go(1,numbers[0])<<endl;
	return 0;
}
