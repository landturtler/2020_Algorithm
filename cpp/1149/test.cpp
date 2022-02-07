#include<iostream>
#include<tuple>
using namespace std;

tuple<int,int,int> a;

int get(int n) {
	return get<n>(a);
}

int main() {
	a = make_tuple(1,2,3);
	cout << get(0)<<endl;
	return 0;
}
