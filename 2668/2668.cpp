//그룹은 총 1개가 나온다.그룹 나눌 생각하지 말고, 이미 방문했었던 노드이면 
#include <iostream>
#include <set>
#define MAX 101
using namespace std;
int N,sum;
int arr[MAX];
bool visited[MAX];
set <int > s;
void go(int st, int end) {
	if( arr[st] == end ) {
		s.insert(st);
		sum++;
		return;
	}
	else if (visited[arr[st]]) return;
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
		go(i,i); //해당 번호로 시작하는 사이클 존재하는지 
	}

	cout << sum <<endl;
	for(auto it : s)
		cout<<it<<endl;

	return 0;

}
