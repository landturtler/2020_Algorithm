#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

vector<int> solution(int N,vector<int> coffee_times) {
	vector<int> answer;
	priority_queue<pair<int,int>,vector<pair<int,int> > ,greater<pair<int,int> > > pq;

	for(int i=0;i<N;i++) 
		pq.push({coffee_times[i],i+1});

	int idx = N; //다음으로 커피머신에 들어갈 index
	while(idx <coffee_times.size()) {
		//가장 작은 값 넣기 
		pair<int,int > min_coffee = pq.front();
		answer.push_back(coffee.second);
		pq.pop();
		//만약 최소 시간이 여러개 있을 경우 넣기 
		while( pq.front() == min_coffee.first) { 
			answer.push_back(pq.front().second);
			pq.pop();
		}
		//큐의 나머지 값을 갱신하기
		

		//새로운 값 삽입 
   }

	while(!pq.empty()) {
		answer.push_back(pq.top().second);
		pq.pop();
	}
	return answer;
}

int main() {
	int N;
	vector<int> answer;
	vector<int> coffee_times;
	
	N = 3;
	coffee_times.push_back(4);
	coffee_times.push_back(2);
	coffee_times.push_back(2);
	coffee_times.push_back(5);
	coffee_times.push_back(3);
	answer = solution(N,coffee_times);
	for(int i=0;i<answer.size();i++) {
		cout<<answer[i]<<" ";
	}
	return 0;
}
