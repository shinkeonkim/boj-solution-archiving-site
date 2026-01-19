#include <iostream>
using namespace std;
int N,K,X,ar[1100][1100];
int main()
{
	scanf("%d %d %d",&N,&K,&X);
	for(int y=1; y<=N; y++)
		for(int x=1; x<=N; x++)
			ar[y][x]=9999999;
			
	for(int x=1; x<=K; x++)
	{
		int a,b,c;
		scanf("%d %d %d",&a,&b,&c);
		if(ar[a][b]>c) ar[a][b]=c;
	}
	
	for(int k=1; k<=N; k++)
	for(int y=1; y<=N; y++)
	for(int x=1; x<=N; x++)
	{
		if(ar[y][x]>ar[y][k]+ar[k][x])
		ar[y][x]=ar[y][k]+ar[k][x];
		if(y==x)ar[y][x]=0;
	}
	
	int Max=0;
	for(int y=1;y<=N; y++)
	{
		if(Max<ar[y][X]+ar[X][y])
		Max=ar[y][X]+ar[X][y];
	}
	printf("%d",Max);
	
}