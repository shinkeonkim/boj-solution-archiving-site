#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;
int M,N,ar[1100][1100],check[1100][1100];
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
queue <int> q;
int main()
{
	cin>>M>>N;
	for(int y=0; y<M; y++)
	{
		for(int x=0; x<N; x++)
		{
			scanf("%1d",&ar[y][x]);
		}
	}
	for(int x=0; x<N; x++)
	{
		if(ar[0][x]==0)
		{
			q.push(x);
			check[0][x]=1;	
		}
	}
	while(!q.empty())
	{
		int X=q.front()%N;
		int Y=q.front()/N;
		q.pop();
		
		for(int d=0; d<4; d++)
		{
			if(-1<dx[d]+X && dx[d]+X<N &&-1<dy[d]+Y && dy[d]+Y<M)
			{
				if(check[dy[d]+Y][dx[d]+X]==0 && ar[dy[d]+Y][dx[d]+X]==0)
				{
					check[dy[d]+Y][dx[d]+X]=1;
					q.push((dy[d]+Y)*N+dx[d]+X);
				}	
			}	
		}
	}
	
	for(int x=0; x<N; x++)
	{
		if(check[M-1][x]==1)
		{
			cout<<"YES";
			return 0;
		}
	}
	cout<<"NO";
}