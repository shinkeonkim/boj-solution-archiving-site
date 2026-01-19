#include <iostream>
using namespace std;
unsigned long long int N,ar[110],D[110][30];
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)cin>>ar[x];
	D[1][ar[1]]=1;
	for(int x=2; x<=N-1; x++)
	{
		for(int y=0; y<=20; y++){
			if(D[x-1][y]>0&&0<=ar[x]+y&&ar[x]+y<=20)
			{
				D[x][y+ar[x]]+=D[x-1][y];
			}
			if(D[x-1][y]>0&&0<=y-ar[x]&&y-ar[x]<=20)
			{
				D[x][y-ar[x]]+=D[x-1][y];
			}
		}
	}
	cout<<D[N-1][ar[N]];
}