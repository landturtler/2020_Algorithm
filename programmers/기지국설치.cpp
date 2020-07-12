#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer=0;
    int left = 1,right;
    for (auto x : stations) {
        int len;
        right = x - w -1;
        if(left <= right ) {
            len = right - left +1;
            if( len <= 2*w +1 ) answer ++;
            else {
                answer +=len/(2*w+1);
                if( len%(2*w+1) !=0 ) answer++;
            }
        }
        left = x + w + 1;
        if( left > n )  break;
    }
    //맨 오른쪽 처리
    if( left <=n ) {
        int len = n - left + 1;
        if( len <= 2*w +1 ) answer++;
        else {
            answer += len/(2*w+1);
            if(len%(2*w+1) !=0 ) answer++; 
        }
    }
    return answer;
}