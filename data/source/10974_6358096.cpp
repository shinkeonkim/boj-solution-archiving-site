#include <stdio.h>
int n,check[10],ar[10];
int f(int y)
{
	if(y>=n)
	{
		for(int x=0; x<n; x++) printf("%d ",ar[x]);
		printf("\n");
	}
	else
	{
		for(int x=1; x<=n; x++)
		{
			if(check[x]==0)
			{
			ar[y]=x;
			check[x]=1;
			f(y+1);
			check[x]=0;
			}
		}
	}
}
int main()
{
	scanf("%d",&n);
	for(int x=1; x<=n; x++)
	{
		check[x]=1;
		ar[0]=x;
		f(1);
		check[x]=0;
	}
}