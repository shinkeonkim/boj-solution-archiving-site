#include <stdio.h>
int ar[20005],n,Cnt;
int main()
{
	scanf("%d",&n);
	for(int x=0; x<n; x++) scanf("%d",&ar[x]);
	for(int x=0; x<n; x++)
	{
		if(x+1!=ar[x])Cnt++;
	}
	printf("%d",Cnt);
}