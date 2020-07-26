/*
14888 
문제:N개의 수와 N - 1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과 중 최댓값과 최솟값 출력
알고리즘 : 완전 탐색(재귀)
*/

#include <iostream>
#include <algorithm>
using namespace std;
const int MAX = 1000000000 + 1;

int N;
int number[12], Operator[4];
int maxResult = -MAX, minResult = MAX;

//cnt: 이번에 계산할 숫자의 number배열에서의 index, sum : 연산이 끝났을 때 결과값
//plus,minus,multiply,divide : 각 연산의 남은 횟수
void DFS(int plus, int minus, int multiply, int divide, int cnt, int sum){ 
	//연산 끝남
	if (cnt == N)	{
		maxResult = max(maxResult, sum);
		minResult = min(minResult, sum);
	}

	if (plus > 0)
		DFS(plus - 1, minus, multiply, divide, cnt + 1, sum + number[cnt]);

	if (minus > 0)
		DFS(plus, minus - 1, multiply, divide, cnt + 1, sum - number[cnt]);

	if (multiply > 0)
		DFS(plus, minus, multiply - 1, divide, cnt + 1, sum * number[cnt]);

	if (divide > 0)
		DFS(plus, minus, multiply, divide - 1, cnt + 1, sum / number[cnt]);
}


int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> number[i];

	for (int i = 0; i < 4; i++)
		cin >> Operator[i];

	DFS(Operator[0], Operator[1], Operator[2], Operator[3], 1, number[0]);

	cout << maxResult << endl;
	cout << minResult << endl;

	return 0;
}