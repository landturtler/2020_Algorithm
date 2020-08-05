#include<iostream>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
map<int, string > m;

string getSum(string a, string b) {
	string ans = "";
	int sum = 0; //올림수
	while (a.size() || b.size() || sum ) {
		if (!a.size() == 0) {
			sum += a.back() - '0';
			a.pop_back();
		}
		if (!b.size() == 0) {
			sum += b.back() - '0';
			b.pop_back();
		}
		ans.push_back((sum % 10) + '0');
		sum /= 10;
	}

	reverse(ans.begin(),ans.end());
	return ans;
}
string fib(int cnt) { //cnt번째 피보나치 수 구하기 
	string s = getSum(m[cnt - 1], m[cnt - 2]);
	m.insert({ cnt,s });
	return s;
}
int main() {
	m.insert({ 1,"1" });
	m.insert({ 2,"1" });

	int cnt = 3;
	while (1) {
		string s = fib(cnt);
		if (s.size() == 1000) {
			cout << cnt;
			break;
		}
		cnt++;
	}
	return 0;
}
