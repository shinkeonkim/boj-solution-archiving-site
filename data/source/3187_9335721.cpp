#include <iostream>
using namespace std;
int R,C,check[300][300],S,W,totalS,totalW;
char ar[300][300];
void DFS(int x,int y)
{
	check[x][y]=1;
	if(ar[x][y]=='v') W++;
	else if(ar[x][y]=='k') S++;
	
	if(x>0)
	{
		if(check[x-1][y]==0&&ar[x-1][y]!='#')
		{
			DFS(x-1,y);
		}
	}
	if(y>0)
	{
		if(check[x][y-1]==0&&ar[x][y-1]!='#')
		{
			DFS(x,y-1);
		}
	}
	if(x+1<R)
	{
		if(check[x+1][y]==0&&ar[x+1][y]!='#')
		{
			DFS(x+1,y);
		}
	}
	if(y+1<C)
	{
		if(check[x][y+1]==0&&ar[x][y+1]!='#')
		{
			DFS(x,y+1);
		}
	}
	return ;
}
int main()
{
	cin>>R>>C;
	for(int x=0; x<R; x++)
		for(int y=0; y<C; y++)
			cin>>ar[x][y];
	
	for(int x=0; x<R; x++)
	{
		for(int y=0; y<C; y++)
		{
			if(check[x][y]==0&&ar[x][y]!='#')
			{
				S=0;W=0;
				DFS(x,y);
				if(S>W) totalS+=S;
				else totalW+=W;
			}
		}
	}
	cout<<totalS<<" "<<totalW;
}