#include <iostream>
#include <algorithm>
using namespace std;
int N,ans,ar[550][550],check[550][550];
int dx[5]={1,-1,0,0},dy[5]={0,0,1,-1};
int DFS(int y,int x)
{
	if(check[y][x]!=-1) return check[y][x];
	
	check[y][x]=1;
	
	for(int z=0; z<4; z++)
	{
		int nexty=y+dy[z];
		int nextx=x+dx[z];
		
		if(1<=nexty&&nexty<=N&&1<=nextx&&nextx<=N)
		{
			if(ar[nexty][nextx]>ar[y][x])
			{
				check[y][x]=max(check[y][x],DFS(nexty,nextx)+1);
			}
		}
	}
	return check[y][x];
}
int main()
{
	cin>>N;
	for(int y=1; y<=N; y++)
		for(int x=1; x<=N; x++)cin>>ar[y][x],check[y][x]=-1;
	
	for(int y=1; y<=N; y++)
	{
		for(int x=1; x<=N; x++)
		{
			if(check[y][x]==-1)
			{
				ans=max(ans,DFS(y,x));
			}
		}
	}
	
	cout<<ans;
}