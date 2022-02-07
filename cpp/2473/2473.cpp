/*

0일 때 -> 바로 나감 
0이 없을 때 -> 벡터에 저장된 sum값이 작으면 업데이트 
이 때, 막연히 작으면 안되고 0과 가까워야 함. 즉 절댓값으로 판단 
*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N;
long long sum = 200000000;
vector<long long> v;
vector<long long> sol(3,0);
bool flag;

void solution() {
	
	long long tot=0;
	for(int i=0;i<3;i++)
	 tot +=v[i];
	
	if( abs(tot) < sum ) {

		for(int i=0;i<3;i++)
		 	sol[i] = v[i];
		sum = abs(tot);

		if(sum == 0 )
			flag = true;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N;
	long long tmp;
	for(int i=0;i<N;i++) {
		cin >> tmp;
		v.push_back(tmp);
	}

	do{
		solution();
		if(flag) break;

	}while(next_permutation(v.begin(),v.end()));

	sort(sol.begin(),sol.end());

	for(auto x : sol)
	 cout <<x<<" ";

	return 0;
}
