#include<iostream>
#include<vector>
#include <cmath>
using namespace std;


int solution(int n,int r, int c) { //2로 나누는 걸 n번 수행해야 한다.
	int se = pow(2,n-1);
	if(n ==0)
		return 0;
	
	else if(r < se) {
		if(c<se) return solution(n-1,r,c);
		else return pow(se,2) + solution(n-1,r,c-se);
	}
	else {
		if(c<se) return pow(se,2)*2 + solution(n-1,r-se,c); 
		else return pow(se,2)*3+ solution(n-1,r-se,c-se);
	}	
}

int main() {
	ios_base ::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n,r,c;
	cin >> n >> r >> c;
	cout<< solution(n,r,c);
	return 0;
}
