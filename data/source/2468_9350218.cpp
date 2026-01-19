#include <iostream>
using namespace std;
int N,ar[110][110],Max,M=1,check[110][110],Cnt;
void DFS(int y,int x)
{
	check[y][x]=1;
	if(y>1&&ar[y-1][x]>0&&check[y-1][x]==0)
	{
		DFS(y-1,x);
	}
	if(x>1&&ar[y][x-1]>0&&check[y][x-1]==0)
	{
		DFS(y,x-1);
	}
	if(y<N&&ar[y+1][x]>0&&check[y+1][x]==0)
	{
		DFS(y+1,x);
	}
	if(x<N&&ar[y][x+1]>0&&check[y][x+1]==0)
	{
		DFS(y,x+1);
	}	
}
int main()
{
	cin>>N;
	for(int y=1; y<=N; y++)
	{
		for(int x=1; x<=N; x++)
		{
			cin>>ar[y][x];
			if(Max<ar[y][x]) Max=ar[y][x];
		}
	}
	for(int z=2; z<=Max; z++)
	{
		for(int y=1; y<=N; y++)
		{
			for(int x=1; x<=N; x++)
			{
				if(ar[y][x]<z)ar[y][x]=0;
			}
		}
		for(int y=1; y<=N; y++)
		{
			for(int x=1; x<=N; x++)
			{
				check[y][x]=0;
			}
		}
		Cnt=0;
		for(int y=1; y<=N; y++)
		{
			for(int x=1; x<=N; x++)
			{
				if(ar[y][x]>0&&check[y][x]!=1)
				{
					Cnt++;
					DFS(y,x);
				}	
			}
		}
		if(Cnt>M) M=Cnt;
	}
	cout<<M;
}