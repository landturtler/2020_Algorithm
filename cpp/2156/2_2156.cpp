/*
2156
DP
dp[num][cnt] : num번호까지 포도주를 마셨을 때(안마셨을 수도 있음) 최대로 마실 수 있는 포도주의 양(cnt는 가장 최근에 연속해서 마신 포도주의 수)
dp[i][0] = dp[i-1][0], dp[i-1][1], dp[i-1][2], 중 큰 값
dp[i][1] = dp[i-1][0] +wine[i]
dp[i][2] = dp[i-1][1] + wine[i]
*/
#include<iostream>
#include<algorithm>
#define MAX 10001
using namespace std;
int dp[MAX][3],wine[MAX];
int N,sum;

//top-down DP
int go(int num,int cnt) {
  if( num < 0 ) return 0;
  else if(dp[num][cnt] != -1) return dp[num][cnt];

  if(cnt >0) dp[num][cnt] = go(num-1,cnt-1)+wine[num];
  else dp[num][cnt] = max({go(num-1,0),go(num-1,1),go(num-1,2)});
  return dp[num][cnt];
}


int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  fill(&dp[0][0],&dp[MAX-1][3],-1);
 
  cin >> N;
  for(int i=0;i<N;i++)
     cin >> wine[i];

  sum = go(N,0); // min({go(N-1,0),go(N-1,1),go(N-1,2)}) 와 같은 의미
  cout<<sum;
     return 0;

}