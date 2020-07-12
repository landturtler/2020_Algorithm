/*
	현재 택시 위치에서 최단 거리인 승객부터 탑승. 거리가 같으면 행, 열이 작은 순서로 진행
	목적지로 도착시, 이동거리 *2로 연료가 충전됨. 만약 가는 도중에 바닥나면 이동 실패
	문제: 모든 손님을 이동시키고 연료 충전했을 때, 남은 연료의 양 출력.실패 시 -1 출력
 잘못 생각 : 그 승객이 타고 나서+ 목적지까지 거리만큼만 충전됨
*/

#include<iostream>
#include<algorithm>
#include <queue>
#include <tuple>
#define MAX 21
#define INF 987654321
using namespace std;
struct person {
	int sx, sy;//시작 좌표 
	int dx, dy;//도착 좌표 
};

person customer[MAX * MAX];
int N, M, oil;
bool road[MAX][MAX];
pair <int, int> taxi; //택시의 현재 좌표 
bool sucess[MAX]; // 탑승 완료시킨 승객의 번호 

pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };

//택시 위치 -> 각 고객 -> 고객 목적지 까지 최단 거리 
int getDir(person& p, int flag) {
	int st_x, st_y, end_x, end_y;
	if (flag == 0) {
		st_x = taxi.first;
		st_y = taxi.second;
		end_x = p.sx;
		end_y = p.sy;
	}
	if (flag == 1) {
		st_x = p.sx;
		st_y = p.sy;
		end_x = p.dx;
		end_y = p.dy;
	}
	if (end_x == st_x && end_y == st_y) return 0;
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	queue<tuple<int, int, int> > q;

	visited[st_x][st_y]= true;
	q.push(make_tuple(st_x,st_y, 0));
	while (!q.empty()) {
		int x = get<0>(q.front());
		int y = get<1>(q.front());
		int dir = get<2>(q.front());
		q.pop();
		if (x == end_x && y == end_y) {
			return dir;
		}
		for (int k = 0; k < 4; k++) {
			int nx = x + d[k].first;
			int ny = y + d[k].second;
			if (nx <= 0 || nx > N || ny <= 0 || ny > N || road[nx][ny] == 1) continue;
			if (!visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_tuple(nx, ny, dir + 1));
			}
		}
	}
    return INF; //도착할 수 없음 
}
//p1이 선택되면 true
bool compare(person& p1, person& p2) {
	if (p1.sx == p2.sx) return p1.sy < p2.sy;
	else return p1.sx < p2.sx;
}

void go() {
	int T = M;
	while (T--) {
		//택시 -> 손님까지 거리가 가장 짧은 손님 선택 
		int select_person = -1;
		int len = INF;
		for (int i = 0; i < M; i++) {
			if (!sucess[i]) {
				int dir = getDir(customer[i],0);
				if (len > dir || (len == dir && compare(customer[i], customer[select_person]))) {
					select_person = i;
					len = dir;
				}
			}
		}
        sucess[select_person] = true;
		//손님을 선택 후, 도착까지 걸리는 거리 계산
		int cost = getDir(customer[select_person], 1);
		//택시 이동 
         
		if ((len + cost) > oil) {
			oil = -1;
			return;
		}

		oil -= (len + cost);
		oil += (cost * 2);
		sucess[select_person] = true;
		taxi.first = customer[select_person].dx;
		taxi.second = customer[select_person].dy;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M >> oil;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> road[i][j];
		}
	}

	int a, b;
	cin >> a >> b;
	taxi = { a,b };

	for (int i = 0; i < M; i++) {
		person p;
		cin >> p.sx >> p.sy >> p.dx >> p.dy;
		customer[i] = p;
	}

	go();
	cout << oil << endl;
	return 0;
}

