#include<iostream>
#include<vector>
#include<cmath>
#include<set>
using namespace std;

int main() {
 /*
	long long cnt =0;
	set<long long> s;
	for(int i=2;i<=100;i++) {
		for(int j=2;j<=100;j++) {
			long long num = pow(i,j);
			if(s.find(num) == s.end()) {
				cnt++;
				s.insert(num);
			}
		}
	}
	cout<<cnt;
*/
	int answer = 0;
	vector<int> squared(101, 0);
	vector<int> dp(101, 0);

	for(int i=2;i<=100;i++)
		for(int j=2;pow(i, j)<=100;j++)
			squared[int(pow(i, j))] = i;
	for(int i=2;i<20;i++)
		cout << i << " " << squared[i] << endl;
	for(int i=2;i<=100;i++){
		if(squared[i] == 0){
			dp[i] = 99;
		} else {
			dp[i] = 99 - dp[squared[i]];
		}
		answer += dp[i];
	}
	cout << answer << endl;
	return 0;
}
