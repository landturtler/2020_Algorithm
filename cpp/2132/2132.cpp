#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int N,sum,idx;
vector<vector<int> > tree(10001);
vector<int> apple; //열매 
vector<int> dp(10001,-1); // x번째 노드에서 시작해서 먹을 수 있는 최대 열매의 수 

int go(int child, int parent) {

	if(dp[child] != -1) return dp[child];
	dp[child] = apple[child]; //자식노드가 없으면 현재 위치가 최대값이므로 현재 노드 열매로 초기화 
	sort(tree[child].begin(), tree[child].end());
	for(int i=0;i<tree[child].size();i++) {
		if(tree[child][i] != parent) // 무한 루프 방지
			dp[child] = max(dp[child],go(tree[child][i],child)+apple[child]);
	}
	return dp[child];
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N;
	int a,b;
	apple.push_back(0);
	for(int i=0;i<N;i++){
		cin>>a;
		apple.push_back(a);
	}

 	for(int i=0;i<N-1;i++) {
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a);
	}
	
	for(int i=1;i<=N;i++) {
		if(dp[i] == -1){
			int result = go(i,-1);
			if(result > sum) {
				sum = result;
				idx = i;
			}
		}
	}
	cout<<sum<<" "<<idx;
	return 0;
}	
