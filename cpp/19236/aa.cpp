#include<iostream>
#define FOR(i,N) for(int i=0;i<N;i++)
using namespace std;

struct fish {
	int x,y;// 좌표 
	int dir; //방향 
	bool live; //살아있는지 유무 
};

int map[4][4]; // 각 위치에 존재하는 물고기의 번호 저장 
pair<int,int> d[9] = {{0,0},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1}};
fish fishes[17]; //각 번호에 해당하는 물고기 정보 저장
int maxSum;

//map에서 상어의 위치는 -1로 한다 
void go(fish shark,int map[4][4],fish *fishes,int sum) {
	maxSum = max(maxSum,sum);
//물고기 이동 
	FOR(i,16) {
		if( fishes[i].live ) {
			FOR(k,9) {
				int nx = fishes[i].x + d[k].first;
				int ny = fishes[i].y + d[k].second;
		//		if( nx < 0 || ny < 0 || nx >= 4 || ny >=4 || map[nx][ny] == -1) continue;	
					//fish[i]는 (nx,ny)로 이동 
				fish tmp = fishes[i];
				int swap_fish = map[nx][ny];
				fishes[i].x = nx;
				fishes[i].y = ny;
				map[nx][ny] = i; //fish[i] 이동 
				fishes[i].dir = (fishes[i].dir+k)%8; //===========이거 확인 
				//(nx,ny)에 물고기가 있다면 swap,없다면 원래 자리는 0으로 비워둠
				if( swap_fish != 0 ) {
					fishes[swap_fish].x = tmp.x;
					fishes[swap_fish].y = tmp.y;
					map[tmp.x][tmp.y] = swap_fish;
				}
				else	map[tmp.x][tmp.y] = 0;		
		//	break;
			}
		}
	}
//상어는 최대 3칸 이동   	

//	FOR(k,3) {

//복구 위해 원래 값 저장 
//	k = 1;
	map[shark.x][shark.y] = 0; //상어는 이제 그 위치에 없다 
		int nx = shark.x + d[shark.dir].first;
		int ny = shark.y + d[shark.dir].second;
	//	if(nx < 0 || nx >= 4 || ny <0 ||ny >=4) break;
		//해당 값을 잡아 먹은 경우를 시뮬레이션 돌리기 
		fish org_shark = shark;
		int org_fish = map[nx][ny];

		shark.x = nx;
		shark.y = ny;
		shark.dir = fishes[org_fish].dir;
		fishes[org_fish].live = false;
		map[nx][ny]=  -1; //새로운 상어의 위치
		go(shark,map,fishes,sum+map[nx][ny]);
		map[nx][ny] = org_fish;
		fishes[org_fish].live = true;
		shark.dir = org_shark.dir;
//	}	
	
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
	fishes[st].live = false;
	map[0][0] = -1;

	go(shark,map,fishes,st);
	cout <<maxSum<<endl;
	return 0;

}

