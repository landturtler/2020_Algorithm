#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
/*
void print(int &arr[4][4]) {
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++)
			cout<<arr[i][j]<<" ";
	cout<<endl;
	}
cout<<endl;
}
*/
void pr(vector<vector<int>> v) {
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++)
			cout<<v[i][j]<<" ";
		cout<<endl;
	}
cout<<endl;

}
void gov(vector<vector<int>> v) {
for(int i=0;i<4;i++)
fill(v[i].begin(),v[i].end(),2);
pr(v);
}
/*
void go(int ar[][4]) {
//	meamset(ar,2,sizeof(ar));
	fill(&ar[0][0],&ar[3][4],2);
	print(ar);
}
*/
int main() {
//	int org[4][4];
	vector<vector<int> > v(4,vector<int>(4,1));
	//afill(&v[0][0],&v[3][4],1);
	for(int i=0;i<4;i++)
		fill(v[i].begin(),v[i].end(),1);
	pr(v);
	gov(v);
	pr(v);

	//memset(org,1,sizeof(org));
	//afill(&org[0][0],&org[3][4],1);
	//print(org);
	//go(org);
//	print(org);
	return 0;
}
