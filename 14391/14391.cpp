/*

처음 생각 :dfs + 완전탐색 
제일 큰 숫자부터 찾아서 탐색 시작

*/
#include<iostream>
using namespace std;
int N,M;
int paper[4][4];
bool cutted[4][4];
pair<int,int> cut

int solve() {
	
	int a=-1,b=-1;
	for(int i=0;i<N;i++) {
	 	for(int j=0;j<M;j++) {
			if(!cutted[i][j]) {
				a = i;
				b = j;
				break;
		 	}
		}
		if( a != -1) break;
	}
	if(a == -1) return 0; //다 자름 

	//안자른 부분 탐색
	int result=0;
	//최대 길이로 만들어서 탐색하기
	cut = {N-i,M-j}; 
	

}

int main() {
	ios_base::sync_with_stdio(false);
	cin >> N >> M;
	
	
	for(int i=0;i<N;i++) {
		string s;
		cin >> s;
		for(int j=0;j<M;j++)
	  		paper[i][j] = s[j]-'0';
	}

}
