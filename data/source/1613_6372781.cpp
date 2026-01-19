#include <iostream>
using namespace std;
int N,K,S,ar[510][510];
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
	scanf("%d",&S);
	for(int k=1; k<=N; k++)
	for(int y=1; y<=N; y++)
	for(int x=1; x<=N; x++)
	{
		if(ar[y][x]>ar[y][k]+ar[k][x])
		ar[y][x]=ar[y][k]+ar[k][x];
		if(y==x)ar[y][x]=0;
	}

	for(int x=0; x<S; x++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		if(ar[a][b]==999999&&ar[b][a]==999999)printf("0\n");
		else if(ar[a][b]==999999) printf("1\n");
		else printf("-1\n");
	}
}