//중간에 코너로 빠지면 그 길로만 가야 한다. 경로는 총 4개
//완전탐색을 통해 max값 찾기 
//중간에 들어왔을 때, 25이후부터는 같은 위치이다.즉, 25,32,40은 같은 위치이다.마지막 40도 같은 위치임을 명심할 것. 

#include<iostream>
#include<algorithm>
using namespace std;

int turn[10]; //각 턴에 해당하는 값 
pair<int,int> mal[4]; //각 말의 경로와 위치 저장 
bool check[36]; // 현재 위치에 다른 말이 존재하는지 
int board[36] = {0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,10,13,16,19,20,22,24,30,28,27,26,25,30,35,40,0};//board[31]=25
int corner[4] ={0,20,24,27};//경로가 바뀌는 지점
int jump[3] = {20,24,27};//0번 경로는 40노드에 해당하는 index으로 jump,1&2번 경로는 25에 해당하는 idx로 jump 
bool is_finish[4]; //각 말이 도착 했는지 
int result;

void solution(int cnt, int sum) {
	if(cnt == 10) {
		result = max(result,sum);
		return;
	}	
	int yut = turn[cnt];
	//이번 turn에 움직일 말 선택 
	for (int i= 0;i<4;i++) {
		if (!is_finish[i]) {
			int cur_pos = mal[i].second;
			int next_pos = mal[i].second + yut;
			// 다음 경로와 위치 구하기 
			if( mal[i].first == 0 && next_pos %5 ==0 ) {
				mal[i].second = corner[next_pos/5]; 
				mal[i].first = next_pos/5;
			}
			else if (jump[mal[i].first] <= next_pos) {
				int tmp = (next_pos - jump[mal[i].first]);
				if(mal[i].first == 0) tmp +=34;
				else tmp += 31;
				next_pos = tmp;
			}
			//이미 그 자리에 다른 말이 있으면 continue;
			if(check[next_pos] )
				continue;
			
			check[cur_pos] = false;
			//해당 말이 도착지점으로 이동했으면
			if(next_pos >= 35){
				is_finish[i] = true;
				solution(cnt+1,sum);
				is_finish[i] = false;
			}
			else {
				mal[i].second = next_pos;
				check[next_pos] = true;
				solution(cnt+1,sum+board[next_pos]);
				check[next_pos] = false;
			}
			check[cur_pos] = true;
			mal[i].second = cur_pos;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
 	for(int i=0;i<10; i++) {
		cin >> turn[i];
	}

	fill(&mal[0],&mal[4],make_pair(0,0));
	fill(&check[0],&check[36],false);
	fill(&is_finish[0],&is_finish[4],false);
	
    solution(0,0);
	cout << result<<endl;
	return 0;
}
