#include <iostream>
using namespace std;
int N,K,ar[110][110];
int main()
{
	scanf("%d %d",&N,&K);
	for(int y=1; y<=N; y++)
		for(int x=1; x<=N; x++)
			ar[y][x]=999999;
			
	for(int x=1; x<=K; x++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		ar[a][b]=1;
	}
	
	for(int k=1; k<=N; k++)
	for(int y=1; y<=N; y++)
	for(int x=1; x<=N; x++)
	{
		if(ar[y][x]>ar[y][k]+ar[k][x])
		ar[y][x]=ar[y][k]+ar[k][x];
		if(y==x)ar[y][x]=0;
	}

	
	for(int y=1;y<=N; y++)
	{
		int Cnt=0;
		for(int x=1; x<=N;x++)
		{
			if(ar[y][x]==999999&&ar[x][y]==999999)Cnt++;
		}
		printf("%d\n",Cnt);
	}
}