#include<iostream>
#include<queue>
#include<tuple>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int A,B,resultA,resultB;
	queue<tuple<int,int,int> > q;

	cin >> A >> B; 
	q.push(make_tuple(A,0,1));
	q.push(make_tuple(0,B,1));
	
	while(!q.empty()) {
		int cnt = get<2>(q.front());
		int a = get<0>(q.front());
		int b = get<1>(q.front());
		q.pop();

		if(a == resultA && b == resultB) {
			cout<<cnt<<endl;
			return 0;
		}
		
	    q.push(make_tuple(A,b,cnt+1));
		q.push(make_tuple(a,B,cnt+1));
		if( a > 0 ) {
			q.push(make_tuple(0,b,cnt+1));
			if( a + b >= B ) q.push(make_tuple(a-(B-b),B,cnt+1));
			else q.push(make_tuple(0,a+b,cnt+1));
		}
		if( b > 0 ){
			q.push(make_tuple(a,0,cnt+1));
			if( a + b  > A ) q.push(make_tuple(A,b-(A-a),cnt+1));
			else q.push(make_tuple(a+b,0,cnt+1));
		}
	}
	
	cout<<-1<<endl;
	return 0;
}

