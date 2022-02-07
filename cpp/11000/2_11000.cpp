#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N,s,e;
	vector<pair<int,int> > v;
	cin >> N;
	for(int i=0;i<N;i++) {
		cin >> s >> e;
		v.push_back({s,e});
	}
	sort(v.begin(),v.end());

	priority_queue<int,vector<int>,greater<vector<int>> > q; //강의실 별 끝나는 시간 저장 
	q.push(v[0].second);
	int i =1;
	for(int i=1;i<N;i++) {
	//i번째 수업을 넣을 수 있는 강의실 찾기
	//가장 빨리 끝나는 수업보다 더 일찍 시작하면 강의실 새로 배정
			if( v[i].first < q.top()) {
				q.push(v[i].second);
			}
	// 수업 종료시간 이후에 수업이 시작하면 
			else {
				q.pop();
				q.push(v[i].second);
			} 
	}
	cout << q.size();
	return 0;

}
