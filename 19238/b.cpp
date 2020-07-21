#include<iostream>
#include<algorithm>
#include <queue>
#include <map>
#include <tuple>
#define MAX 21
#define INF 98765
using namespace std;
int src[MAX][MAX], dest[MAX][MAX],road[MAX][MAX]; //손님들의 출발지, 도착지 저장 
int N, M;
long oil;
pair <int, int> taxi;//택시 좌표
bool success[MAX]; //해당 손님을 탑승 완료했는지 
pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };

//거리 구하기 (flag = 0이면 가장 가까운 손님 구하기, 1이면 목적지까지 거리 구하기)
pair<int,pair<int,int> > getDis(bool flag, const pair<int,int> p) {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	
	if( flag == 0 )	{
	priority_queue<tuple<int, int, int>,vector< tuple<int,int,int> > > q; 
	}
	else { queue<tuple<int,int,int> > q;}

	visited[p.first][p.second] = true;
	q.push(make_tuple(0, p.first, p.second));

	while (!q.empty()) {
		int dir = get<0>(q.top());
		int x = get<1>(q.top());
		int y = get<2>(q.top());
		q.pop();
		if (!flag && src[x][y] != -1 && !success[src[x][y]]) {
			if (dir > oil)return { -1,{0,0} };
			else return { dir,{x,y} };
		}
		
		//손님을 태우고 목적지에 도착할 수 있는지 확인 
		else if (flag && (dest[x][y] == src[p.first][p.second])) {
			if (dir > oil) return { -1,{0,0} };
			else return { dir,{x,y} };
		}

		for (int k = 0; k < 4; k++) {
			int nx = x + d[k].first;
			int ny = y + d[k].second;
			if (nx <= 0 || nx > N || ny <= 0 || ny > N || road[nx][ny] == 1) continue;
			if (!visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_tuple(dir+1,nx,ny));
			}
		}
	}
	return { -1,{0,0} };
 }


void go() {
	int T = M;
	while (T--) {
		//1. 현재 택시에서 가장 가까운 거리 & 손님 좌표 구하기 
		pair<int, pair<int,int> > to_customer = getDis(0,taxi); 
		int select_person = src[to_customer.second.first][to_customer.second.second]; // 선택된 손님 번호
		cout<<"선택된 손님 번호:"<<select_person+1<<endl;
		int len1 = to_customer.first; // 택시 -> 손님 거리
		if ( len1 == -1) {
			oil = -1;
			return;
		}
		//2. 선택된 손님 -> 목적지까지 거리 구하기  
		pair<int,pair<int,int> > to_dest  = getDis(1,to_customer.second); // 손님 - > 목적지 거리 
		int len2 = to_dest.first;
		pair<int,int> dest = to_dest.second;
		if (len2 == -1) {
			cout<<"len2 = -1 ";
			oil = -1;
			return;
		}
		cout<<"oil = "<<oil<<", len1 = "<<len1<<", len2 = "<<len2<<"  ";
		oil -= (len1 + len2);
		oil += (len2 * 2);
		cout<<"운전 후 oil = "<<oil<<endl;
		success[select_person] = true;
		taxi.first = dest.first;
		taxi.second = dest.second;
	}
	oil = -1;
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
	int a,b;
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
