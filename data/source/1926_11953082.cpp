#include <iostream>
using namespace std;
int N,M,ar[550][550];
int dy[]={0,0,1,-1};
int dx[]={1,-1,0,0};
int Cnta,Cntb,Max;
void DFS(int Y,int X)
{
	Cntb++;
	ar[Y][X]=0;
	for(int d=0; d<4; d++)
	{
		if(0<=Y+dy[d]&&Y+dy[d]<N&&0<=X+dx[d]&&X+dx[d]<M)
		{
			if(ar[Y+dy[d]][X+dx[d]]==1)
			{
				DFS(Y+dy[d],X+dx[d]);	
			}	
		}
	}
}
int main()
{
	cin>>N>>M;
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<M; x++)
		{
			cin>>ar[y][x];
		}
	}
	
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<M; x++)
		{
			if(ar[y][x]==1)
			{
				Cnta++;
				Cntb=0;
				DFS(y,x);
				if(Cntb>Max) Max=Cntb;
			}
		}
	}
	cout<<Cnta<<endl<<Max; 
}