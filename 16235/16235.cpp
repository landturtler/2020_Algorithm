#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 11
#define FOR(i,n) for(int i =1;i<=n;i++)

using namespace std;
int N;
int A[MAX][MAX]; //겨울마다 제공되는 양분 
vector<int> trees[MAX][MAX];
pair<int, int > dir[8] = { {-1,0},{0,1},{1,0},{0,-1},{-1,1},{-1,-1},{1,-1},{1,1}};

int go(int K) {
	vector<int> die[MAX][MAX];	//죽은 나무들 
	int food[MAX][MAX];  //현재 양분
	FOR(i,N)
		fill(food[i],food[i]+MAX,5);

	while(K--) {
/*	
  
	cout <<"K = "<<K<<endl;
	cout <<"현재까지 남은 나무들 정보 :"<<endl;
	FOR(i,N) {
		FOR(j,N) {
			if(!trees[i][j].empty()){
				cout<<"좌표 ("<<i<<","<<j<<") :"<<endl;
				for(auto x : trees[i][j])	
					cout<<x<<" ";
			cout<<endl<<"-----나무 정보 끝---"<<endl;
			}
		}
	}

	cout <<"현재까지 남은 양분들 정보 : "<<endl;
	FOR(i,N) {
		FOR(j,N){
			cout<<food[i][j]<<" ";
		}
		cout<<endl;
	}
cout<<endl;
*/
	//봄 : 양분 & 나이 먹기  
        FOR(i,N ) {
			FOR(j,N) {
				if( trees[i][j].empty()) continue;
                sort(trees[i][j].begin(),trees[i][j].end());
                
				int &fd = food[i][j]; // (i,j)의 현재 양분
				for(auto it = trees[i][j].begin();it != trees[i][j].end();it++ ) {
					if( *it > fd ) { 
                       // cout <<"현재 ("<<i<<","<<j<<")의 양분은"<<fd<<"인데";
					//	cout<< "해당 좌표에 나이"<<*it<<"인 나무가 있어서 죽음"<<endl;
						die[i][j].resize((int)distance(it,trees[i][j].end()));
						copy(it,trees[i][j].end(),die[i][j].begin());
						trees[i][j].erase(it,trees[i][j].end());//erase 함수 
						break;
					}
					fd -= *it;
					(*it)++;
				}
			}
		}

		//여름 : 죽은 나무들의 나이/2만큼 양분에 추가 
		FOR(i,N) {
			FOR(j,N) {
				if(die[i][j].empty()) continue;
				for(auto x : die[i][j]) {
					food[i][j] += x/2;
				}
				die[i][j].clear();
			}
		}
		
		//가을 : 나무의 확장 
		FOR(i,N) {
			FOR(j,N) {
				for(auto x : trees[i][j]) {
					if(x % 5 == 0) {
						for(int k =0 ;k<8;k++) {
							int ni = i + dir[k].first;
							int nj = j + dir[k].second;
						   if( ni <= 0 || nj <=0 || ni > N ||nj > N) continue;
						   trees[ni][nj].push_back(1);
					   }
				   }
			   }
		   }
	   }

	   //겨울 : 양분 제공
	   FOR(i,N) {
			FOR(j,N)
				food[i][j] += A[i][j];		
		}
	}

	//살아 남은 나무 수 찾기
	int sum = 0;
	FOR(i,N) {
		FOR(j,N) {
			if(trees[i][j].empty()) continue;
			sum += trees[i][j].size();
		}
	}
	return sum;
}

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int M,K;
	cin >> N >> M >> K;
	//양분 배열 입력 받음
	for(int i=1;i<=N; i++) {
		for(int j = 1; j<=N;j++) 
			cin >> A[i][j];		
	}

	//각 나무 정보 입력 받음 
	for(int i =1; i <=M; i++) {	
		int r,c,old;
		cin >> r >> c >> old;
		trees[r][c].push_back(old);
	}
	
	cout << go(K)<<endl;
    
	return 0;
}
