#include <iostream>
using namespace std;
int N,ar[1010][10],Min=99999999,Memo[1010][10],ar2[1010][10];
int f(int n,int x)
{
	if(Memo[n][x]) return Memo[n][x];
	else if(n==1)
	{
		return Memo[n][x]=ar[n][x];
	}
	else
	{
		int mm=99999999;
		for(int y=0; y<3; y++)
		{
			if(x!=y)
			{
				if(ar[n][x]+f(n-1,y)<mm) mm=ar[n][x]+f(n-1,y);
			}
		}
		return Memo[n][x]=mm;
	}
	
}
int main()
{
	scanf("%d",&N);
	for(int x=1; x<=N; x++)
	{
		for(int y=0; y<3; y++)scanf("%d",&ar[x][y]);
	}
	
	for(int x=0; x<3; x++)
	{
		if(Min>f(N,x)) Min=f(N,x);
	}
	for(int x=1; x<=N; x++)
	{
		for(int y=0; y<3; y++) ar2[N-x+1][y]=ar[x][y];
	}
	for(int x=1; x<=N; x++)
	{
		for(int y=0; y<3; y++) ar[x][y]=ar2[x][y];
	}
	for(int x=0; x<3; x++)
	{
		if(Min>f(N,x)) Min=f(N,x);
	}
	
	printf("%d",Min);
}