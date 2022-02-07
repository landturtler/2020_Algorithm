#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int answer = 0, max_euler = 28123;
	vector<bool> possible(max_euler, 0);
	vector<int> temp(max_euler, 0);
	vector<int> euler;
	for(int i=1;i<max_euler;i++){
		if(temp[i] > i)
			euler.push_back(i);

		for(int j=i;j<max_euler;j+=i){
			temp[j] += i;
		}
	}
	for(int i=0;i<euler.size();i++){
		for(int j=i;j<euler.size();j++){
			if(euler[i]+euler[j] < max_euler)
				possible[euler[i]+euler[j]] = true;
		}
	}
	
	for(int i=max_euler-1;i>0;i--){
		if(!possible[i]){
			answer += i;
		}
	}
	cout << answer << endl;
	return 0;
}
