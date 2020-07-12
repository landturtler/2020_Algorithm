/*
문제: 하노이의 탑. 판의 개수 N이 주어질 때, 옮긴 횟수 K를 출력하라
알고리즘 :재귀 호출
*/
#include<iostream>
#include<cmath>
#include<string>

using namespace std;

string bigNumAdd(string num1, string num2)
{
	long long sum = 0;
	string result;
	string _result;
	//1의 자리부터 더하기 시작한다
	while (!num1.empty() || !num2.empty() || sum)
	{
		if (!num1.empty())
		{
			sum += num1.back() - '0';
			num1.pop_back();
		}
		if (!num2.empty())
		{
			sum += num2.back() - '0';
			num2.pop_back();
		}
		//다시 string 형태로 만들어 push_back
		result.push_back((sum % 10) + '0');
		sum /= 10;
	}

	for (int i = 0; i < result.length(); i++)
	{
		char temp;
		temp = result[result.length()-i-1];
		_result.push_back(temp);
	}
	return _result;
}

//2의 n승은 0으로 끝날 수 없으므로
string subtractOne(string num) {
	int back = num.back() - '0';
	num.pop_back();
	back -= 1;
	num.push_back(back + '0');
	return num;
}

void hanoi(int N,int from,int tmp, int to) {
	if(N == 1)
		cout <<from <<" "<<to<<"\n";
	else {
		hanoi(N-1,from,to,tmp);
		cout <<from<<" "<<to<<"\n";
		hanoi(N-1,tmp,from,to);
	}	
}

void solution(int N) {
	
	if(N<=20) {
		cout <<pow(2,N)-1<<"\n";
		hanoi(N,1,2,3);
	}
	else {
		string num = "2";
		for(int i=0;i<N-1;i++) {
			string temp = bigNumAdd(num,num);
			num = temp;
		}
		cout<<subtractOne(num)<<"\n";
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	int n; cin >> n;
	solution(n);
	return 0;
}
