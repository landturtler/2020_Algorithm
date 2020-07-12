//이동할 수 없으면 이동하지 않는다. 
//
#include<iostream>
#define FOR(i,N) for(int i=0;i<N;i++)
using namespace std;

void print(int map[4][4]) {

	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
		cout<<map[i][j]<<" ";
	}
	cout<<endl;
	}
cout<<endl;
}

struct fish {
	int x,y;// 좌표 
	int dir; //방향 
	bool live; //살아있는지 유무 
};

int map[4][4]; // 각 위치에 존재하는 물고기의 번호 저장 
pair<int,int> d[9] = {{0,0},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1}};
fish fishes[17]; //각 번호에 해당하는 물고기 정보 저장
int maxSum;

void go(fish shark,int map[4][4],fish *fishes,int sum) {
	cout <<"sum = "<<sum<<endl;
	maxSum = max(maxSum,sum);

//물고기 이동(이동할 순서인 물고기는 방향, 좌표만 바뀌는 거고, 
	for(int i =1; i<=16;i++) {
		if( fishes[i].live ) {
				fishes[i].dir--;
				fish tmp = fishes[i]; //원래 이동할 물고기 번호 
			for(int k =0;k<8;k++){	
				fishes[i].dir = fishes[i].dir+1 == 9 ? 1 : fishes[i].dir +1;
				int nx = fishes[i].x + d[fishes[i].dir].first;
				int ny = fishes[i].y + d[fishes[i].dir].second;
				if( nx < 0 || ny < 0 || nx >= 4 || ny >=4 || map[nx][ny] == -1) continue;	
				int swap_fish = map[nx][ny]; //바꿀 물고기 
				fishes[i].x = nx;
				fishes[i].y = ny;
				map[nx][ny] = i; 
				if( swap_fish != 0 || fishes[swap_fish].live ) {
					fishes[swap_fish].x = tmp.x;
					fishes[swap_fish].y = tmp.y;
					map[tmp.x][tmp.y] = swap_fish;
				}
				else	map[tmp.x][tmp.y] = 0;		
			break;
			}

		}
	}
	print(map);
//상어 이동 
	FOR(k,3) {
//복구 위해 원래 값 저장	
		map[shark.x][shark.y] = 0; //상어는 이제 그 위치에 없다 
		int nx = shark.x + d[shark.dir].first; 
		int ny =shark.y + d[shark.dir].second;

		if(nx < 0 || nx >= 4 || ny <0 ||ny >=4 ||!fishes[map[nx][ny]].live) break;
		//해당 값을 잡아 먹은 경우를 시뮬레이션 돌리기 
		
		int org_fish = map[nx][ny]; //상어가 이번에 잡아먹을 물고기 
		fish org_shark = shark; //복구 위해 원래 값 저장 
		shark.x = nx; 
		shark.y = ny;
		shark.dir = fishes[org_fish].dir;
		//cout<<"이동할  상어 위치 : "<<shark.x<<","<<shark.y<<endl;
		fishes[org_fish].live = false;
		map[nx][ny]=  -1; //새로운 상어의 위치
		cout <<"상어는 "<<nx<<","<<ny<<"를 잡아먹음"<<endl;
		go(shark,map,fishes,sum+org_fish);
		map[nx][ny] = org_fish;
		fishes[org_fish].live = true;
		shark.dir = org_shark.dir;
		cout<<"상어가 "<<nx<<","<<ny<<"잡아먹은거 취소 "<<endl;
	}	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	//물고기 정보 입력받음 
	FOR(i,4) {
		FOR(j,4) {
			fish tmp;
			cin >> map[i][j]; // 물고기 저장 
			cin >> tmp.dir;
			tmp.x = i;
			tmp.y = j;
			tmp.live = true;
			fishes[map[i][j]] = tmp;
		}
	}
	//맨 처음 상어는 (0,0)에서 시작
	fish shark;
	int st = map[0][0];
	shark.x = 0;
	shark.y = 0;
	shark.dir = fishes[st].dir;
	shark.live = true;
	fishes[st].live = false;
	shark.dir = fishes[st].dir;
	map[0][0] = -1;

	go(shark,map,fishes,st);
	cout <<maxSum<<endl;
	return 0;
}

