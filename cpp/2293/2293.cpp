#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int go(int num,int *dp, vector<int> &v) {
	if(num == 0) return 1; //한 가지 경우의 수가 만들어 졌다는 의미
	if(num < 0 ) return 0;
	if( dp[num] ) return dp[num];
	for(int i=0;i<v.size();i++) {
		dp[num] += go(num - v[i],dp,v); //num-i가 아니라 v[i]
		cout << "dp["<<num<<"] +=" <<go(num-v[i],dp,v)<<endl;
	}
	cout<<"dp["<<num<<"] = "<<dp[num]<<endl;
	return dp[num];
}
/*
int go(int num,vector<int> &v) {
	int sum=0;
	while(sum >= num) {
		for(int i=0;i
	}

}
*/
int solution(int k,vector<int> &v) {
	sort(v.begin(),v.end());
	int dp[k+1] = {0,};
	return go(k,dp,v);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL); cout.tie(NULL);

	int n,k;
	cin >> n >> k;
	vector<int> v(n);
	for(int i=0;i<n;i++)
		cin >> v[i];
	cout<<solution(k,v);
	return 0;


}
