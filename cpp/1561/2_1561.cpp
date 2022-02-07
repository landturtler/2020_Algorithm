#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
long long N,le,ri;
int M;
int rides[10001];


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	le = 0;
	ri =20000000000000;
	int M;
	int rides[10001];

	cin >> N >> M;
	for(int i=0;i<M;i++)
		cin >>rides[i];

	long long mid,cnt,T;
	while(le <= ri) {
		cnt = M;
		mid = (le + ri)/2;
		for(int i=0;i<M;i++) cnt += mid /rides[i];
		if(cnt < N) le = mid +1;
		else{
			T = mid;
			ri = mid-1;
		}
	}
	 //T초에 N번째 승객이 탑승 했으므로, T-1초까지 승객 인원 구한 후, N번째 승객이 타는 index 구하기 
	cnt = M;
	for(int i=0;i<M;i++) cnt += (T-1)/rides[i]; //cnt : T-1초까지 탄 승객 수
	for(int i=0;i<M;i++) {
		if(T % rides[i] == 0 ) cnt++;
		if( cnt == N) {
			cout<<i+1;
			break;
		}
     }  
	return 0;
}

