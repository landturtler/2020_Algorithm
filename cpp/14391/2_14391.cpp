#include<iostream>
#include<algorithm>
using namespace std;
int N,M,sum;
int paper[4][4];
bool shape[4][4];//가로 1 세로 0

void getSum() {
	int tot = 0;
	
	for(int i=0;i<N;i++) {
	 int num=0;
	 for(int j=0;j<M;j++) {
		if(shape[i][j]) {
			num *=10;
			num +=paper[i][j];
		}
		else { //연속 깨짐 
			tot +=num;
			num =0; 
		}
	 }
	tot += num;
    }
   
	for(int i=0;i<N;i++) {
		int num2=0;
		for(int j=0;j<M;i++) {
		//	if(shape[i][j] == false) {
		//		num2 *=10;
		//		num2 += paper[i][j];
		//	}
		//	else { //연속 깨짐
				tot += num2;
				num2 = 0; 
		//	}
		}
		tot += num2;
	}
	
	sum = max(sum,tot);
}



void dfs(int x,int y) {
	if( x >= N) {
		getSum();
		return;
	}
	//다음 행 넘어가기
	else if( y >= M) {
		dfs(x+1,0);
		return;
	}
	else { 
	shape[x][y] = true;
	dfs(x,y+1);
	shape[x][y] = false;
	dfs(x,y+1);
	}
}

int main() {
	cin >> N >> M;
	for(int i=0;i<N;i++) {
		string s;
		cin >>s;
		for(int j=0;j<M;j++)
		 paper[i][j] = s[j]-'0';
	}
	
	dfs(0,0);
	cout <<sum;

}
