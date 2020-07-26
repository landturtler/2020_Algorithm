#include<iostream>
#include<cstring>
using namespace std;

int N;
bool map[101][101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	memset(map, 0, sizeof(map));

	cin >> N;
	for(int i=0;i<N;i++) {
		for(int j=0;j<N;j++){
			cin >> map[i][j];
		}
	}
	for(int x=0;x<10;x++){
		for(int i=0;i<N;i++){
		 	for(int j=0;j<N;j++){
			 	for(int k=0;k<N;k++){
				 	if(k!=i && k!=j)
					 	map[i][j] = map[i][j] || (map[i][k] && map[k][j]);
					
				}
			}
		}
	}

	for(int i=0;i<N;i++){
	 	for(int j=0;j<N;j++){
		 	cout << map[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
