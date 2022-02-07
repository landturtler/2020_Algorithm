#include<iostream>
#define FOR(i,N) for(int i=0;i<N;i++)
using namespace std;


struct fish {
	int x,y;// 좌표 
	int di; //방향 
	bool live; //살아있는지 유무 
};

vector< int > map[4][4]; // 각 위치에 존재하는 물고기의 번호 저장 
pair<int,int> dir[9] = {{0,0},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1}};
fish fishes[17]; //각 번호에 해당하는 물고기 정보 저장
int eating(fish &shark) {
		
		

} 

//map에서 상어의 위치는 -1로 한다 
int move(int x,int y) {
	int sum =0; //상어가 먹은 물고기 번호의 합 
	fish shark; //상어의 위치,이동방향 
	
	while(1) {
	//상어 이동 & 물고기 먹음 
  // 각 이동을 하면서 최댓값을 찾아야 함ㅠㅠ 
	//이동할 수 있는 좌표는 최대 4칸
	FOR(k,4) {
		map[shark.x][shark.y] = 0; //상어는 이제 그 위치에 없다 
		shark.x += dir[di];
		shark.y += dir[di];
		if(nx < 0 || nx >= 4 || ny <0 ||ny >=4) break;
		//해당 값을 잡아 먹은 경우를 시뮬레이션 돌리기 
		fishes[map[nx][ny]].live = false;

		map[nx][ny]=  -1; //새로운 상어의 위치 
	}
}
void move() { 
		FOR(i,16) {
		if( fishes[i].live ) {
			FOR(k,9) {
				int nx = fish[i].x + dir[k].first;
				int ny = fish[i].y + dir[k].second;
				if( nx < 0 || ny < 0 || nx >= 4 || ny >=4 || map[nx][ny] == -1) continue;
				//map에서 fish[i]와 (nx,ny)에 위치한 물고기를 swap한다.	
					fish tmp = fishes[i];
					fishes[i].x = nx;
					fishes[i].y = ny;
					map[fishes[i].x][fishes[i].y] = map[nx][ny];
					fishes[i].di = k%9; //방향 이동 이거 맞는지 확인 
					if(map[nx][ny] !=0 ) {
						fishes[map[nx][ny]].x = tmp.x;
						fishes[map[nx][ny]].y = tmp.y;
						map[nx][ny] = i;
					}
				}
			}
		}	
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	//물고기 정보 입력받음 
	fish eat;
	FOR(i,4) {
		FOR(j,4) {
			fish tmp;
			cin >> map[i][j]; // 물고기 저장 
			cin >> tmp.di;
			tmp.x = i;
			tmp.y = j;
			tmp.live = true;
			fishes[map[i][j]] = tmp;
		}
	}

	cout << move(0,0) <<endl;
	return 0;

}

