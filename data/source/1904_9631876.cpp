#include <iostream>
using namespace std;
int N,ar[1100000][2];
int main()
{
	cin>>N;
	ar[1][1]=1;
	ar[1][0]=0;
	ar[2][1]=1;
	ar[2][0]=1;
	for(int x=3; x<=N; x++)
	{
		ar[x][1]=(ar[x-1][0]+ar[x-1][1])%15746;
		ar[x][0]=(ar[x-2][0]+ar[x-2][1])%15746;
	}
	cout<<(ar[N][1]+ar[N][0])%15746;
}