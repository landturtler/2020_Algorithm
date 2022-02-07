#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>

#define INF 987654321
using namespace std;

int n;
vector<tuple<int,int,int> > v(1000,tuple<int,int,int>{INF,INF,INF}); //색, 비용 저장 
vector<tuple<int,int,int> > color;

int go(int num,int col) { //num번째 집을 col색으로 바꿀때 최소 비용 
	if(num <0) return 0;
	if(get<col>(v[num]) != INF) return get<col>(v[num]);
	get<col>(v[num]) = get<col>(color[num]) + min(go(num-1,(col+1)%3), go(num-1,(col+2)%3));
	return get<col>(v[num]);
}

int solution(int n) {
	tuple<int,int,int> a = {get<0>(color[0]),get<1>(color[0]),get<2>(color[0])};
	v[0] = a;
	int ret =min({go(n-1,0),go(n-1,1),go(n-1,2)});
	return ret;
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	cin >> n;
	int a,b,c;
	for(int i=0;i<n;i++) {
		cin >>a >> b >> c;
		color.push_back(make_tuple(a,b,c));
		cout <<solution(n)<<endl;
	}
}
