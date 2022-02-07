/*
다음 수가 여러개일 땐 A, 구할 수 없을 땐 B
*/

#include<iostream>
#define MAX 51
using namespace std;
int N;
int arr[MAX];

void go() {
	if(N==1){
	 	cout << "A\n";
		return;
	}
	if(arr[0] == arr[1]){
	 for(int i=1;i<N;i++)
	  if(arr[i] != arr[i-1]){
	   cout << "B\n";
	   return;
	  }
	  cout << arr[0] << "\n";
	}
	if(N==2){
	 cout << "A\n";
	 return;
	}
	if((arr[2]-arr[1])%(arr[1]-arr[0]) != 0){
	 cout << "B\n";
	 return;
	}
	int a = (arr[2]-arr[1])/(arr[1]-arr[0]);
	int b = arr[1] - a * arr[0];
	for(int i=3;i<N;i++){
	 if(arr[i] != arr[i-1]*a + b){
	  cout << "B\n";
	  return;
	 }
	}
	cout << arr[N-1]*a + b << "\n";
	/*
	//같은 수만 반복되는 경우
	if(N < 3) {
		cout<<"A";
		return;
	}
	if(arr[0] == arr[1] ) {
		cout<<arr[0];
		return;
	}
	//연립 방정식을 만들 수 있는 경우 
	else if(N>=3) {
		//a,b 구하고 for문 돌리다가 a,b 규칙이 성립하지 않으면 B 출력
		double a = (arr[2] - arr[1]) / (arr[1] - arr[0]);
		double b = arr[1] - a*arr[0];
		if(a -(int)a !=0 || b - (int)b != 0 ) {
			cout<<"B";
			return;
		}

		for(int i =3;i<N;i++) {
			if(arr[i] != arr[i-1]*a+b) {
				cout<<"B";
				return;
			}
		}
		cout<<arr[N-1]*a+b;
		return;
	}
	*/
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;
	for(int i=0;i<N;i++)
		cin >> arr[i];
	
	go();
	return 0;

}
