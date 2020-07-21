/*
11047
그리디
*/

#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, K, coins[10],cnt=0;
    cin >> N >> K;
	for(int i=0;i<N;i++)
		cin >> coins[i];

    for (int i = N-1; i >= 0; i--) {
        //큰 값의 동전부터 최대한 사용하기 
            cnt += (K / coins[i]);
            K %= coins[i];
            if(K == 0) break;
    }
    cout << cnt;
}
