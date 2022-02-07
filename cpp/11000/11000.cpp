#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N;
	vector<pair<long long,long long> > cla;
	multiset<int> room; //각 강의실 별 수업 끝나는 시간 저장 
	cin >> N;
	for(int i=0;i<N;i++) {
		pair<long long,long long> a;
		cin >> a.first >>a.second;
		cla.push_back(a);
	}
	sort(cla.begin(),cla.end());
	room.insert(cla[0].second); //0번 강의실에는 맨 처음 강의 넣기 
	
	for(int i=1;i<N;i++) {
		pair<long long,long long > c = cla[i];
		bool flag = true;
		for(multiset<int>::iterator it = room.begin();it !=room.end();) {
			if(c.first >= *it) {
				room.erase(it++);
				room.insert(c.second);
				flag = false;
				break;
			}
			else it++;
		}
		if(flag) room.insert(c.second);
	}
	cout <<room.size()<<endl;
	return 0;
}

