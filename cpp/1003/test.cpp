#include<iostream>
#include<vector>

using namespace std;

int main() {
pair<int,int> a,b;
a = make_pair(1,1);
b = make_pair(2,2);
a += b;	
cout<<"a = "<<a.first<<","<<a.second;
return 0;
}
