#include<iostream>
#include<algorithm>
#include <queue>
#include <map>
#include <tuple>
#define MAX 21
#define INF 98765
using namespace std;
int src[MAX][MAX], dest[MAX][MAX], road[MAX][MAX]; //손님들의 출발지, 도착지 저장 
int N, M;
long oil;
pair <int, int> taxi;//택시 좌표
bool success[MAX]; //해당 손님을 탑승 완료했는지 
pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };


pair<int,pair<int,int> > getDis(pair <int,int> &p) {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	queue<tuple<int, int, int> > q;
	visited[p.first][p.second] = true;
	q.push(make_tuple(0, p.first, p.second));
	while (!q.empty()) {
		int dir = get<0>(q.front());
		int x = get<1>(q.front());
		int y = get<2>(q.front());
		q.pop();
		if (dest[x][y] == src[p.first][p.second] ) {
			if (dir > oil)return { -1,{0,0} };
			else return { dir,{x,y} };
		}

		for (int k = 0; k < 4; k++) {
			int nx = x + d[k].first;
			int ny = y + d[k].second;
			if (nx <= 0 || nx > N || ny <= 0 || ny > N || road[nx][ny] == 1) continue;
			else if (!visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_tuple(dir + 1, nx, ny));
			}
		}
	}
	return { -1,{0,0}};
}
pair<int, pair<int,int> > selectPerson() {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	priority_queue<tuple<int, int, int>, vector< tuple<int, int, int> >,greater<tuple<int,int,int> >> q;
	
	visited[taxi.first][taxi.second] = true;
	q.push(make_tuple(0, taxi.first, taxi.second));

	while (!q.empty()) {
		int dir = get<0>(q.top());
		int x = get<1>(q.top());
		int y = get<2>(q.top());
		q.pop();
		if (src[x][y] != -1 && !success[src[x][y]]) {
			if (dir > oil)return { -1,{0,0} };
			else return { dir,{x,y} };
		}

		for (int k = 0; k < 4; k++) {
			int nx = x + d[k].first;
			int ny = y + d[k].second;
			if (nx <= 0 || nx > N || ny <= 0 || ny > N || road[nx][ny] == 1) continue;
			else if (!visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_tuple(dir + 1, nx, ny));
			}
		}
	}
	return { -1,{0,0} };
}


void go() {
	int T = M;
	while (T--) {
		//acout<<"택시 좌표:("<<taxi.first<<","<<taxi.second<<") ";
		//1. 현재 택시에서 가장 가까운 거리 & 손님 좌표 구하기 
		pair<int, pair<int, int> > to_customer = selectPerson();
		int select_person = src[to_customer.second.first][to_customer.second.second]; // 선택된 손님 번호
	//	cout<<"선택한 손님 번호 : "<<select_person+1<<" ";
		int len1 = to_customer.first; // 택시 -> 손님 거리
		if (len1 == -1) {
			oil = -1;
			return;
		}
		//2. 선택된 손님 -> 목적지까지 거리 구하기  
		pair<int, pair<int,int > > dest = getDis(to_customer.second); // 손님 - > 목적지 거리 
		int len2 = dest.first;
		if (len2 == -1) {
			oil = -1;
			return;
		}
		if( len1 + len2 > oil) {
			oil = -1;
			return;
		}
		oil -= (len1 + len2);
		oil += (len2 * 2);
		success[select_person] = true;
		taxi.first = dest.second.first;
		taxi.second = dest.second.second;
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	fill(&src[0][0], &src[MAX - 1][MAX], -1);
	fill(&dest[0][0], &dest[MAX - 1][MAX], -1);

	cin >> N >> M >> oil;
	//지도 구축
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> road[i][j];
		}
	}
	//택시 정보 입력
	int a, b;
	cin >> a >> b;
	taxi = { a,b };
	//각 손님의 출발지, 목적지 저장 
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		src[a][b] = i;
		cin >> a >> b;
		dest[a][b] = i;
	}
	go();
	cout << oil << endl;
	return 0;


}
