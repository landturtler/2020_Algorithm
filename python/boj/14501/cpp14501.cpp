#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
 int N;
 cin >> N;
 vector<int> day = vector<int>(N + 1, 0);
 vector<int> pay = vector<int>(N + 1, 0);

 for(int i=0;i<N;i++)
  cin >> day[i] >> pay[i];
 
 vector<int> dp(N + 1, 0);
 for(int i=0;i<N;i++){
  for(int j=i+day[i];j<=N;j++){
   dp[j] = max(dp[j], dp[i] + pay[i]);
  }
 }
 cout << dp[N] << endl;
}
