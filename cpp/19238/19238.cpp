/*
	현재 택시 위치에서 최단 거리인 승객부터 탑승. 거리가 같으면 행, 열이 작은 순서로 진행
	목적지로 도착시, 이동거리 *2로 연료가 충전됨. 만약 가는 도중에 바닥나면 이동 실패
	문제: 모든 손님을 이동시키고 연료 충전했을 때, 남은 연료의 양 출력.실패 시 -1 출력 
*/

#include<iostream>
#include <queue>
#define MAX 21
#define INF 987654321
using namespace std;
struct person{
	int sx,sy;//시작 좌표 
	int dx,dy;//도착 좌표 
};

person customer[MAX*MAX];
int N,M,oil;
bool road[MAX][MAX]; 
pair <int,int> taxi; //택시의 현재 좌표 
bool sucess[MAX]; // 탑승 완료시킨 승객의 번호 

pair<int, int> d[4] = {{-1,0},{1,0},{0,1},{0,-1} };

//택시 위치 -> 각 고객까지 최단 거리 
int getDir(person &p) {
	if(p.dx == taxi.first && p.dy == taxi.second) return 0;

	bool visited[MAX][MAX];
	fill(&visited[0][0],&visited[MAX-1][MAX],false);
	queue<tuple<int,int,int> > q;
	
	visited[taxi.first][taxi.second] = true;
	q.push( make_tuple(taxi.first,taxi.second,0 ));
	while(!q.empty()) {
		int x = get<0>(q.front());
		int y = get<1>(q.front());
		int dir = get<2>(q.front());
		q.pop();
		if( x == p.dx && y == p.dy) return dir;
		
		for(int k=0; k<4;k++) {
			int nx = x + d[k].first;
			int ny = y + d[k].second;
			if(nx <= 0 || nx >N || ny <=0 || ny > N || board[nx][ny] == 1) continue; 
			if(!visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_tuple(nx,ny,dir+1));
			}
	}
	
}

//p1이 선택되면 true
bool compare(person &p1, person &p2) {
	if (p1.sx  == p2.sx ) return p1.sy < p2.sy;
	else return p1.sx < p2.sy;
}

void go() {
	while(--M) {
	//현재 위치에서 가장 가까운 승객 구하기 
		pair<int,int>len = {INF,-1 }; //거리 ,승객 번호 
		for(int i=0; i<M;i++) {
			int dir = getDir(customer[i]);
			if(!sucess[i] ) {
				if( len.first > dir || (len.first == dir && compare(customer[i],customer[len.second]))){
					len.second = i;
					len.first = getDir(customer[i]);
				}
 			}
		}
	//택시 이동 
		if(len.first > oil) {
			cout <<"M = "<<M<<"일 때 실패"<<endl;
			oil = -1;
			return;
		}
		cout<<"oil"<<oil<<"에 "<<len.first<<"만큼 충전됨"<<endl;
		sucess[len.second] = true;
		oil += len.first;
		taxi.first = customer[len.second].dx;
		taxi.second = customer[len.second].dy;
	}	
 	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M >>oil;

	for (int i=1;i <=N;i++) {
		for(int j =1;j<=N;j++) {
			cin >>road[i][j];
		}
	}

	int a,b;
	cin >> a >> b;
	taxi = {a,b};

	for (int i=0;i<M;i++){
		person p;
		cin >> p.sx >>p.sy >> p.dx >>p.dy;
		customer[i] = p;
	}

	go();
	cout <<oil<<endl;
	return 0;
}
