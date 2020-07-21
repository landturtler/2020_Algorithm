#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


vector<int> solution(int N,vector<int> coffee_times) {
	vector<int> answer;
	vector<pair<int,int> > machine;

	for(int i=0;i<N;i++) 
		machine.push_back({coffee_times[i],i+1});

	int idx = N; //다음으로 커피머신에 들어갈 index
	while(idx<coffee_times.size()) {
		sort(machine.begin(),machine.end());
		pair<int,int > coffee = machine[0];

		for(int i=0;i<machine.size();i++) {
			machine[i].first -= coffee.first;
			if( machine[i].first == 0 ) {
				answer.push_back(machine[i].second);
				machine[i].first = coffee_times[idx]; //새로운 커피값 삽입 
				machine[i].second = idx+1;
				if(++idx == coffee_times.size()) break;
			}
		}
	}

	sort(machine.begin(),machine.end());
	for(int i=0;i<machine.size();i++)
		answer.push_back(machine[i].second);

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
