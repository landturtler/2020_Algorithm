#include<iostream>
#include<queue>
#include<vector>
using namespace std;
long long N;
int M;

int go( vector<int> rides) {
	priority_queue<pair<int,int>,vector< pair<int,int> >,greater< pair<int,int > > >pq; //놀이기구의 남은 시간,해당 놀이기구를 탄 사람의 idx
	
	//맨 처음 놀이기구를 탐 
	for(int i=0;i<M;i++)
		pq.push({rides[i],i+1});
	
	long long idx=M+1; //다음에 탈 사람 idx

	while(!pq.empty()){
		pair<int,int> person = pq.top();
		pq.pop();
		pq.push({ person.first*2,person.second});
		idx++;
		if(idx == N+1) return person.second;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	vector<int> rides(10000,0);
	int result;

	cin >> N >> M;
	for(int i=0;i<M;i++) 
		cin >> rides[i];

	result = go(rides);
	cout<<result;
	return 0;

}
