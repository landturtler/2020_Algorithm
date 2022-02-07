#include<iostream>
using namespace std;

int solution(int n) {
	if( n < 0 ) return 0;
	if( n ==0 ) return 1;
	else return solution(n-1) + solution(n-2) + solution(n-3);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	int T,n;
	cin >> T;
		while(T--) {
			cin >>n;
			cout<<solution(n)<<endl;
	}	
	return 0;
}
