#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main() {

	vector<int> v;
	for(int i=0;i<=9;i++)
	 v.push_back(i);

	 int cnt =0;
	 long long answer =0;
	 
	 do {
	 	if(++cnt == 1000000) {
	 		for(int i=0;i<v.size();i++) {
				answer *= 10;
				answer += v[i];
			}
			break;
    	}	
	 }while(next_permutation(v.begin(),v.end()));

	cout << answer<<endl;
	return 0;
}
