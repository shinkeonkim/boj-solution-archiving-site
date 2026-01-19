#include <iostream>
using namespace std;
int T,N,K,ar[22][22];
void f()
{
	for(int x=0; x<20; x++) ar[0][x]=x;
	for(int y=1; y<20; y++)
	{
		ar[y][1]=ar[y-1][1];
		for(int x=2; x<20; x++)
		{
			ar[y][x]=ar[y][x-1]+ar[y-1][x];
		}
	}
}
int main()
{
	cin>>T;
	f();
	for(int x=0; x<T; x++) 
	{
		cin>>N>>K;
		cout<<ar[N][K]<<endl;
	}
}