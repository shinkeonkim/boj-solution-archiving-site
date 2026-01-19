#include <iostream>
using namespace std;
int N,ar[110][110];
int main()
{
	scanf("%d",&N);
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<N; x++)
		{
			scanf("%d",&ar[y][x]);
			if(ar[y][x]==0) ar[y][x]=99999;
		}
	}
	for(int k=0; k<N; k++)
	for(int y=0; y<N; y++)
	for(int x=0; x<N; x++)
	{
		if(ar[y][x]>ar[y][k]+ar[k][x])
		ar[y][x]=ar[y][k]+ar[k][x];
	}
	
	for(int y=0;y<N; y++)
	{
		for(int x=0; x<N;x++)
		{
			if(ar[y][x]==99999) printf("0 ");
			else printf("1 ");
		}printf("\n");
	}
	
}