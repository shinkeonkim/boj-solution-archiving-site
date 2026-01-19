#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int N,M,check[10],ar[10];
int Save[1100000][10],Cnt;
void P()
{
	for(int x=1; x<=M; x++) 
	{
		Save[Cnt][x]=ar[check[x]];
	}
	Cnt++;
}
int f(int k)
{
	if(k==M)
	{
		for(int x=1; x<=N; x++)
		{
			check[k]=x;
			P();
		}
	}
	else if(k==1)
	{
		for(int x=1; x<=N; x++)
		{
			check[k]=x;
			f(k+1);
		}
	}
	else
	{
		for(int x=1; x<=N; x++)
		{
			check[k]=x;
			f(k+1);
		}
	}
}
int main()
{
	cin>>N>>M;
	for(int x=1; x<=N; x++) cin>>ar[x];
	sort(ar+1,ar+N+1);
	
	if(M==1)
	{
		for(int x=1; x<=N; x++)
		{
			printf("%d\n",ar[x]);
		}
		return 0;
	}
	f(1);
	for(int x=0; x<Cnt; x++)
	{
		for(int y=1; y<=M; y++)
		{
			printf("%d ",Save[x][y]);
		}
		printf("\n");
	}
}