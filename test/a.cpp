#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int solution( vector<int>goods, vector<int>box) {
	sort(goods.begin(),goods.end());
	sort(box.begin(),box.end());

	int cnt=0;
	int idx = 0;
	for(int i=0;i<box.size();i++) {
		if(idx >= goods.size()) break;
		else if(box[i] >= goods[idx]) {
			cnt++;
			idx++;
		}
	}
	return cnt;
}

int main() {
	vector<int> goods;
	vector<int> box;
	
	goods.push_back(3);
	goods.push_back(8);
	goods.push_back(6);
	box.push_back(5);
	box.push_back(6);
	box.push_back(4);

	int result = solution(goods,box);
	cout <<result;
	return 0;
}
