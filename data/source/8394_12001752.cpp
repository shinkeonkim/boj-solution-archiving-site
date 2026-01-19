#include <iostream>
using namespace std;
int N;
int D[11000000][2]; // [i][0]은 안한경우, [i][1]은 i-1번째 사람솨 악수한 경우  
int main()
{
	cin>>N;
	D[1][0]=1;
	D[1][1]=0;
	for(int x=2; x<=N; x++)
	{
		D[x][0]=(D[x-1][0]+D[x-1][1])%10;
		D[x][1]=D[x-1][0]%10;	
	} 
	cout<<(D[N][0]+D[N][1])%10;
}