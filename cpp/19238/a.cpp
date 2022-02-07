#include<iostream>
#include<algorithm>
#include <queue>
#include <tuple>
#define MAX 21
#define INF 98765
using namespace std;
struct person {
	int sx, sy;
	int dx, dy;
};

person customer[MAX * MAX];
int N, M;
long oil;
bool road[MAX][MAX];
pair <int, int> taxi; 
bool success[MAX]; //�ش� �մ��� ž�� �Ϸ��ߴ��� 
pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };

//�Ÿ� ���ϱ� 
int getDis(person& p, int flag) {
	int st_x=0, st_y=0, end_x=0, end_y=0;
	//�ý� -> �մ� �Ÿ� ���ϱ� 
	if (flag == 0) {
		st_x = taxi.first;
		st_y = taxi.second;
		end_x = p.sx;
		end_y = p.sy;
	}
	//�մ� �¿��� ���������� �Ÿ� ���ϱ� 
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

	visited[st_x][st_y] = true;
	q.push(make_tuple(st_x, st_y, 0));
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
	return -1; 
}

//�Ÿ��� ���� �� �� �� ��
bool compare(person& p1, person& p2) {
	if (p1.sx == p2.sx) return p1.sy < p2.sy;
	else return p1.sx < p2.sx;
}

void go() {
	int T = M;
	while (T--) {
		int select_person = -1;
		int len = INF;
		for (int i = 0; i < M; i++) {
			if (!success[i]) {
				int dir = getDis(customer[i], 0); // �ý� -> �մԱ��� �Ÿ� ���ϱ�
				if (dir == -1) continue;
				if (select_person == -1 || len > dir || (len == dir && compare(customer[i],customer[select_person]))) {
					select_person = i;
					len = dir;
				}
			}
		}
		//���� ���: ���� �߿� ���ᰡ �������ų�, �մ��� �¿� �� ���ų�, �մ� �¿��µ� �� �� ���ų�
		if (select_person == -1) {
			oil = -1;
			return;
		}
		int cost = getDis(customer[select_person], 1);
		if (cost == -1 || len + cost > oil) {
			oil = -1;
			return;
		}

		oil -= (len + cost);
		oil += (cost * 2);
		success[select_person] = true;
		taxi.first = customer[select_person].dx;
		taxi.second = customer[select_person].dy;
	}
	oil = -1;
	return;
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

