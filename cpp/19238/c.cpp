#include<iostream>
#include<algorithm>
#include <queue>
#include <map>
#include <tuple>
#define MAX 21
#define INF 98765
using namespace std;
int src[MAX][MAX], dest[MAX][MAX],road[MAX][MAX]; //�մԵ��� �����, ������ ���� 
int N, M;
long oil;
pair <int, int> taxi;//�ý� ��ǥ
bool success[MAX]; //�ش� �մ��� ž�� �Ϸ��ߴ��� 
pair<int, int> d[4] = { {-1,0},{1,0},{0,1},{0,-1} };

//�Ÿ� ���ϱ� (flag = 0�̸� ���� ����� �մ� ���ϱ�, 1�̸� ���������� �Ÿ� ���ϱ�)
pair<int,pair<int,int> > getDis(bool flag, const pair<int,int> p) {
	bool visited[MAX][MAX];
	fill(&visited[0][0], &visited[MAX - 1][MAX], false);
	priority_queue<tuple<int, int, int>,vector< tuple<int,int,int> > > q;

	visited[p.first][p.second] = true;
	q.push(make_tuple(0, p.first, p.second));

	while (!q.empty()) {
		int dir = get<0>(q.top());
		int x = get<1>(q.top());
		int y = get<2>(q.top());
		q.pop();
		
		// �ش� ��ǥ�� �մ��� �ִ���, �� �մԱ����� ������ �� �ִ��� Ȯ��
		if (!flag && src[x][y] != -1 && !success[src[x][y]]) {
			if (dir > oil) return { -1,{0,0} };
			else return { dir,{x,y} };
		}
		
		//�մ��� �¿�� �������� ������ �� �ִ��� Ȯ�� 
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
				q.push(make_tuple(dir+1, nx, ny));
			}
		}
	}
	return { -1,{0,0} };
}


void go() {
	int T = M;
	while (T--) {
		cout << "���� �ý� ��ġ: "<<;: 
		//1. ���� �ýÿ��� ���� ����� �Ÿ� & �մ� ��ǥ ���ϱ� 
		pair<int, pair<int,int> > to_customer = getDis(0,taxi); 
		int select_person = src[to_customer.second.first][to_customer.second.second]; // ���õ� �մ� ��ȣ
		int len1 = to_customer.first; // �ý� -> �մ� �Ÿ�
		if ( len1 == -1) {
			oil = -1;
			return;
		}
		//2. ���õ� �մ� -> ���������� �Ÿ� ���ϱ�  
		pair<int,pair<int,int> > to_dest  = getDis(1,to_customer.second); // �մ� - > ������ �Ÿ� 
		int len2 = to_dest.first;
		pair<int,int> dest = to_dest.second;
		if (len2 == -1) {
			oil = -1;
			return;
		}

		oil -= (len1 + len2);
		oil += (len2 * 2);
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
	//���� ����
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> road[i][j];
		}
	}
	//�ý� ���� �Է�
	int a,b;
	cin >> a >> b;
	taxi = { a,b };
	//�� �մ��� �����, ������ ���� 
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

