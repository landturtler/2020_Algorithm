
#include <iostream>
#include <set>
#define MAX 101
using namespace std;
int N,sum;
int arr[MAX];
bool visited[MAX]; //방문 했는지 
set <int > cycle; //사이클을 이루는 노드들 저장 
void go(int st, int end) {
	if( visited[arr[st]]) return;//사이클을 이루지 못함 

	else if( arr[st] == end ) {
		cycle.insert(st);
		sum++;
		return;
	}

	visited[arr[st]] = true;
	go(arr[st],end);
}


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);

	cin >> N;
	for(int i= 1;i<=N;i++)
		cin >> arr[i];

	for(int i=1;i<=N;i++) {		
		fill(&visited[0],&visited[MAX],false);
		go(i,i); //해당 번호가 포함된 사이클 존재하는지 
	}

	cout << sum <<endl;
	for(auto it : cycle)
		cout<<it<<endl;

	return 0;

}
