#include<iostream>
#include<vector>
using namespace std;


//일의 자리 수를 0 또는 9로 맞춰주는 함수 
void mak(long long *cnt, long long st, long long ten) {
	while(n >0) {
		cnt[n%10] += ten;
		n /= 10;
	}
}

void get(long long st,long long end,long long ten,long long *cnt) { //st부터 end까지 수 중 ten자리 범위에서 각 숫자가 몇 번 쓰였는지 구함 

//st의 일의자리 수를 0으로 바꾸기(+하면서 0 만들기) 
	while(st %10 !=0 && st <=end) {
		mak(cnt,st,ten);
		st += 1;
	}
	if( start > end) return;

//end의 일의 자리 수를 9로 바꾸기 
	while(end %10 !=9 && start<=end) {
		mak(cnt,end,ten);
		end -=1;
	}

//이제 0으로 시작 ~9로 끝나는 수로 만들었으므로, ten자리에서 각 숫자가 나온 횟수 구하기 
	long long num = (end/10- start/10 +1);
	for(int i=0;i<=9;i++) 
		cnt[i] += num*ten;
	
	get(st/10,end/10,ten*10LL,cnt);//그 다음 범위 수 구하기 
}

void solution(int n) {
	long long cnt[10]={0,}; //각 숫자별 나타난 횟수 저장 
	get(1,n,1,cnt); //1~N범위 중 1의 자리에 각 숫자는 몇 번 쓰였는가 
	for(int i=0;i<10;i++) 
		cout<<cnt[i]<<" ";
	cout <<endl;
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	long long n;
	cin >> n;
	solution(n);
	return 0;
}
