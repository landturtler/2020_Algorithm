/*
1696
BFS
*/
#include<iostream>
#include<algorithm>
#include<queue>
#define MAX 100001
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	int N, K,result = MAX;
	queue<pair< int, int> > q;	
	bool visited[MAX];
	fill(&visited[0],&visited[MAX],false);
		
	cin >> N >> K;

	visited[N] = true;
	q.push({N,0}); //현재 좌표 N부터 시작
	while (!q.empty()) {
		int cur = q.front().first; //현재 위치
		int curCnt = q.front().second; //현재까지 이동한 횟수
		q.pop();
		if (cur == K) {
			result = curCnt;
			break;
		}
		if (cur+1<MAX && !visited[cur + 1]) { 
			visited[cur + 1] = true;
			q.push({cur + 1, curCnt + 1});
		}
		if (cur-1>=0 && !visited[cur - 1]) {
			visited[cur - 1 ] = true;
			q.push({cur -1, curCnt + 1});
		}
		if (2*cur < MAX && !visited[2*cur]){
			visited[2*cur] = true;
			q.push({2*cur, curCnt + 1});
		}
	}
	cout << result;
	return 0;
}
