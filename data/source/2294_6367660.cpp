#include <iostream>
using namespace std;
int ar[100100],coin[120],n,k;
int f(int x)
{
	if(ar[x])return ar[x];
	else if(x==0) return ar[x]=0;
	else
	{
		int Min=999999;
		for(int y=0; y<n; y++)
		{
			if(x-coin[y]>=0)
			{
				int z=f(x-coin[y])+1;
				if(z<Min) Min=z;
			}
		}
		return ar[x]=Min;
	}
}
int main()
{
	scanf("%d %d",&n,&k);
	for(int x=0; x<n; x++)scanf("%d",&coin[x]);
	
	int ww=f(k);
	if(ww!=999999) printf("%d",ww);
	else printf("-1");
}