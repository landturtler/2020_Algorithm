#include<iostream>
#include<queue>
#include<map>
#define MAX 21
#define INF 987654321
using namespace std;

//범위 & 입출력 관련 정보
int N, M, oil;
pair<int, int> taxi; //택시 좌표
bool road[MAX][MAX]; //지도 좌표

//손님 관련 정보
map<pair<int, int>,int> who; //(x,y)에 몇 번 손님이 서있는지 
map<int, pair<int, int> >where; //(째 손님은 어디로 가는지 
bool success[MAX * MAX]; //해당 번호의 손님을 탑승 완료 시켰는지 

pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };


//택시에서 가장 가까운 승객까지 거리 & 승객 번호 리턴 
pair<int,int> selPerson() {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	priority_queue<tuple<int, int, int>, vector< tuple<int, int, int> >, greater<tuple<int, int, int> >> q;
	visited[taxi.first][taxi.second] = true;
	q.push(make_tuple(0, taxi.first, taxi.second));

	while (!q.empty()) {
		int dir = get<0>(q.top());
		int x = get<1>(q.top());
		int y = get<2>(q.top());
		q.pop();
		
		//만약 해당 위치에 손님이 있고, 탑승하지 않았던 번호이면 해당 손님 선택
		auto it = who.find({ x,y });
		if (it != who.end() && !success[it->second]) {
			return { dir,it->second };
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
	return { INF,INF };
}

//승객 태우고 목적지까지 거리 출력 
int getDis(int sel_person) {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	queue<tuple<int, int, int> > q;
	
	//sel_person의 현재 위치 찾아내기
	pair<int, int > cur;
	for (auto x : who) {
		if (x.second == sel_person) {
			cur = x.first;
			break;
		}
	}
	visited[cur.first][cur.second] = true;
	q.push(make_tuple(0, cur.first, cur.second));

	while (!q.empty()) {
		int dir = get<0>(q.front());
		int x = get<1>(q.front());
		int y = get<2>(q.front());
		q.pop();

		if (x == where[sel_person].first && y == where[sel_person].second)
			return dir;

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
	return INF;
}

void go() {
	int T = M;
	while (T--) {
		pair<int,int> shortest = selPerson();
		int len1 = shortest.first;
		int sel_person = shortest.second; //선택한 승객 번호
		if (len1 > oil || sel_person == INF ) {
			oil = -1;
			return;
		}
		//손님의 목적지까지 거리 구함
		int len2 = getDis(sel_person);
		if (len1 + len2 > oil) {
			oil = -1;
			return;
		}

		oil -= (len1 + len2);
		oil += (len2 * 2);

		success[sel_person] = true;
		taxi.first = where[sel_person].first;
		taxi.second = where[sel_person].second;

	}
	//모든 승객을 다 태웠는지 확인 
	for (int i = 0; i < M; i++) {
		if (!success[i]) {
			oil = -1;
			return;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M >> oil;
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++)
			cin >> road[i][j];
	}

	int a, b;
	cin >> a >> b;
	taxi = { a,b };

	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		who.insert({ {a,b}, i });
		cin >> a >> b;
		where.insert({ i,{ a,b } });
	}
	go();
	cout << oil << endl;
	return 0;
}